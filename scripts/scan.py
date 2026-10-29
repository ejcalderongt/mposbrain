"""Evidence-indexed Java/XML scanner. It exports identifiers/provenance, never source literals or secrets."""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET
from tree_sitter import Language, Parser
import tree_sitter_java

ROOT = Path(__file__).resolve().parents[1]
A = '{http://schemas.android.com/apk/res/android}'
T = '{http://schemas.android.com/tools}'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(source, *args):
    return subprocess.check_output(['git', '-C', str(source), *args], stderr=subprocess.DEVNULL).decode('utf-8', 'replace').strip()


def walk(node):
    yield node
    for child in node.named_children:
        yield from walk(child)


def layer(path, cls):
    if '/firebase/' in path: return '06-realtime'
    if any('/' + p + '/' in path for p in ('fel', 'felesa', 'felpana')): return '07-fiscal'
    if '/webapi/' in path or '/webservice' in path: return '05-integration'
    if '/ladapt/' in path: return '02-presentation'
    if '/mant/' in path: return '03-catalogs'
    if '/base/' in path and cls.startswith('BaseDatos'): return '04-persistence'
    if '/classes/' in path and (cls.endswith('Obj') or cls.startswith('XML')): return '04-persistence'
    if '/classes/' in path and cls.startswith(('clsDoc', 'clsRep', 'clsPrint', 'clsPrn')): return '08-printing'
    if '/mpos/' in path: return '01-application'
    return '09-platform-shared'


def domain(name):
    patterns = [
        ('restaurant', r'^(Res|Salon)|FacturaRes|Comanda|Mesa|Cortesia'),
        ('cash-payments', r'Caja|Cierre|FinDia|Pago|Cobro|Billetera|Cupon|Card|Tarjeta|Depos|Apertura'),
        ('inventory', r'Inv|Exist|Stock|Traslad|Mov|Almacen'),
        ('sales-orders', r'Venta|Factura|Pedido|Cliente|Cli|Devol|Anula|Bon|Promo|Desc'),
        ('sync-configuration', r'^Main|^Menu|WS|Sync|Envio|Rec|Config|Util|Instala|Diagnos|Tablas|Login|Valida')]
    for label, pattern in patterns:
        if re.search(pattern, name, re.I): return label
    return 'support-catalogs'


def safe_id(text):
    return text if re.fullmatch(r'[A-Za-z_$][A-Za-z0-9_.$]*(?:\(\))?', text) else '<expression>'


def ref(path, node):
    return {'file': path, 'line': node.start_point.row + 1, 'end_line': node.end_point.row + 1}


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def write_rows(name, rows):
    path = ROOT / 'catalog' / (name + '.jsonl')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n' for r in rows), encoding='utf-8')


def scan(source):
    source = source.resolve()
    parser = Parser(Language(tree_sitter_java.language()))
    inventory, classes, methods, calls, navigation, layouts, handlers = [], [], [], [], [], [], []
    globals_access, sql_access, schema, risks, menus, country_sites = [], [], [], [], [], []
    method_by_id, class_by_simple = {}, defaultdict(list)
    declarations = {'class_declaration', 'interface_declaration', 'enum_declaration'}
    sql_pattern = re.compile(r'\b(FROM|JOIN|UPDATE|INTO|TABLE)\s+(?:IF\s+NOT\s+EXISTS\s+)?\[?([A-Za-z_][A-Za-z0-9_]*)', re.I)
    for file in sorted((source / 'app/src/main/java').rglob('*.java')):
        path = file.relative_to(source).as_posix()
        raw = file.read_bytes()
        data = raw.removeprefix(b'\xef\xbb\xbf')
        tree = parser.parse(data)
        text = lambda node: data[node.start_byte:node.end_byte].decode('utf-8', 'replace') if node else ''
        package = next((text(n).removeprefix('package ').rstrip(';').strip() for n in tree.root_node.named_children if n.type == 'package_declaration'), '')
        inv = {'file': path, 'sha256': sha(raw), 'bytes': len(raw), 'lines': data.count(b'\n') + 1,
               'parse_has_error': tree.root_node.has_error, 'layer': layer(path, file.stem)}
        inventory.append(inv)
        current_class, current_method = [None], [None]

        def predicates(node):
            found = []
            parent = node.parent
            while parent:
                condition = parent.child_by_field_name('condition') if parent.type in ('if_statement', 'while_statement', 'for_statement') else None
                if condition:
                    raw_condition = text(condition)
                    found.append({'line': condition.start_point.row + 1, 'sha256': sha(raw_condition.encode()),
                                  'globals': sorted(set(re.findall(r'\b(?:gl|ggl)\.(\w+)', raw_condition))),
                                  'country_literals': sorted(set(re.findall(r'"(HN|GT|SV|PA)"', raw_condition)))})
                parent = parent.parent
            return found

        def visit(node, owner=None, method=None):
            if node.type in declarations:
                name = text(node.child_by_field_name('name'))
                full = (owner + '$' + name) if owner else (package + '.' + name)
                superclass = text(node.child_by_field_name('superclass')).removeprefix('extends ').strip()
                row = {**ref(path, node), 'name': name, 'class': full, 'extends': superclass,
                       'layer': layer(path, name), 'domain': domain(name)}
                classes.append(row); class_by_simple[name].append(full); owner = full
            if node.type in ('method_declaration', 'constructor_declaration'):
                name = text(node.child_by_field_name('name'))
                mid = f'{path}:{node.start_point.row+1}:{name}'
                params = node.child_by_field_name('parameters')
                row = {**ref(path, node), 'id': mid, 'class': owner, 'name': name,
                       'parameters': [{'type': text(p.child_by_field_name('type')), 'name': text(p.child_by_field_name('name'))}
                                      for p in (params.named_children if params else []) if p.type in ('formal_parameter', 'spread_parameter')],
                       'return_type': text(node.child_by_field_name('type')), 'layer': inv['layer'], 'tables': []}
                methods.append(row); method_by_id[mid] = row; method = mid
            if node.type == 'method_invocation':
                name = text(node.child_by_field_name('name'))
                receiver = safe_id(text(node.child_by_field_name('object'))) if node.child_by_field_name('object') else 'this'
                row = {**ref(path, node), 'from_method': method, 'class': owner, 'method': name, 'receiver': receiver,
                       'resolution': 'unresolved', 'candidate_targets': []}
                calls.append(row)
                args = node.child_by_field_name('arguments')
                argtext = text(args)
                if name == 'setContentView':
                    for layout in re.findall(r'R\.layout\.(\w+)', argtext):
                        layouts.append({**ref(path, node), 'class': owner, 'layout': layout, 'method': method})
                if name in ('execSQL', 'OpenDT', 'openDT', 'rawQuery', 'getWritableDatabase', 'getReadableDatabase', 'beginTransaction', 'endTransaction', 'setTransactionSuccessful'):
                    sql_access.append({**ref(path, node), 'method': method, 'operation': name, 'tables': []})
                if name in ('addMenuItem', 'add') and args:
                    children = args.named_children
                    if len(children) >= 2 and children[0].type in ('decimal_integer_literal', 'string_literal') and children[1].type == 'string_literal':
                        # Labels are not exported: a location/id is enough to find the real menu label.
                        item = text(children[0]).strip('"')
                        if re.fullmatch(r'\d{1,5}', item):
                            menus.append({**ref(path, node), 'class': owner, 'method': method, 'item_id': item, 'predicates': predicates(node)})
                if name == 'buildPrint' and node.parent and node.parent.type == 'expression_statement':
                    risks.append({**ref(path, node), 'method': method, 'pattern': 'unchecked_document_result', 'status': 'candidate_requires_review'})
                if name == 'getLaunchIntentForPackage' and args:
                    package_name = argtext.strip('()" ')
                    if re.fullmatch(r'[a-zA-Z][\w]*(?:\.[\w]+)+', package_name):
                        navigation.append({**ref(path, node), 'from_class': owner, 'from_method': method,
                                           'target': package_name, 'kind': 'external_app_candidate', 'predicates': predicates(node), 'runtime': 'unobserved'})
            if node.type == 'object_creation_expression' and text(node.child_by_field_name('type')).split('.')[-1] == 'Intent':
                args = node.child_by_field_name('arguments')
                for child in walk(args) if args else []:
                    if child.type == 'class_literal':
                        target = text(child).removesuffix('.class')
                        navigation.append({**ref(path, node), 'from_class': owner, 'from_method': method, 'target': target,
                                           'kind': 'intent_candidate', 'predicates': predicates(node), 'runtime': 'unobserved'})
            if node.type == 'field_access':
                obj, field = text(node.child_by_field_name('object')), text(node.child_by_field_name('field'))
                if obj in ('gl', 'ggl') and field:
                    parent = node.parent
                    is_write = parent and ((parent.type == 'assignment_expression' and parent.child_by_field_name('left') == node) or parent.type == 'update_expression')
                    rhs = parent.child_by_field_name('right') if is_write else None
                    globals_access.append({**ref(path, node), 'class': owner, 'method': method, 'field': field,
                                           'access': 'write' if is_write else 'read',
                                           'boolean_value': text(rhs) if rhs and rhs.type in ('true', 'false') else None})
            if node.type == 'string_literal':
                literal = text(node)
                for match in sql_pattern.finditer(literal):
                    table = match.group(2).upper()
                    if table in ('SET', 'IF', 'WHERE', 'SELECT', 'AND'): continue
                    sql_access.append({**ref(path, node), 'method': method, 'operation': match.group(1).upper(), 'tables': [table]})
                    if method: method_by_id[method]['tables'].append(table)
                if re.search(r'https?://', literal):
                    risks.append({**ref(path, node), 'method': method, 'pattern': 'http_literal' if 'http://' in literal else 'https_literal',
                                  'status': 'inventory', 'literal_sha256': sha(literal.encode())})
                country = literal.strip('"')
                if country in ('HN', 'GT', 'SV', 'PA'):
                    country_sites.append({**ref(path, node), 'method': method, 'class': owner, 'country': country})
            if node.type in ('assignment_expression', 'variable_declarator'):
                rhs = node.child_by_field_name('right') or node.child_by_field_name('value')
                strings = [text(n).strip('"') for n in walk(rhs) if n.type == 'string_literal'] if rhs else []
                combined = ''.join(strings)
                create = re.search(r'CREATE\s+TABLE\s+\[?(\w+)\]?\s*\((.*)', combined, re.I | re.S)
                if create:
                    columns = re.findall(r'(?:^|,)\s*\[?(\w+)\]?\s+(INTEGER|INT|REAL|TEXT|NUMERIC|VARCHAR(?:\(\d+\))?|CHAR(?:\(\d+\))?|DOUBLE|FLOAT|DATETIME|BIGINT|BLOB|DECIMAL(?:\([^)]*\))?)', create.group(2), re.I)
                    schema.append({**ref(path, node), 'table': create.group(1).upper(), 'columns': [{'name': n.upper(), 'type': t.upper()} for n,t in columns],
                                   'definition_sha256': sha(combined.encode()), 'status': 'static_ddl_not_live_schema'})
                lhs = text(node.child_by_field_name('left') or node.child_by_field_name('name'))
                if re.search(r'(password|passwd|gmps|api_?key|secret|token|llave)', lhs, re.I) and strings:
                    risks.append({**ref(path, node), 'method': method, 'pattern': 'credential_like_literal_assignment',
                                  'identifier': safe_id(lhs), 'status': 'private_source_review_required_no_value_exported'})
            if node.type == 'catch_clause':
                body = node.child_by_field_name('body')
                content = text(body)
                pattern = 'empty_catch' if body and not [c for c in body.named_children if c.type not in ('line_comment', 'block_comment')] else None
                if not pattern and not re.search(r'DiagnosticLog|\bLog\.|addlog|msgbox|Toast|throw\b|printStackTrace', content): pattern = 'catch_without_obvious_reporting'
                if pattern: risks.append({**ref(path, node), 'method': method, 'pattern': pattern, 'status': 'candidate_not_confirmed_defect'})
            if node.type in ('ERROR',) or node.is_missing:
                risks.append({**ref(path, node), 'pattern': 'parser_gap', 'status': 'manual_review_required'})
            for child in node.named_children: visit(child, owner, method)

        visit(tree.root_node)

    by_class_name = defaultdict(list)
    for method in methods:
        method['tables'] = sorted(set(method['tables']))
        by_class_name[(method['class'], method['name'])].append(method['id'])
    for call in calls:
        candidates = by_class_name.get((call['class'], call['method']), []) if call['receiver'] in ('this', 'super') else []
        if call['receiver'] == 'super': candidates = []  # inheritance needs type resolution, not a name-only guess
        if candidates:
            call['resolution'] = 'same_class_name_candidates_not_overload_resolved'; call['candidate_targets'] = candidates
    manifest = ET.parse(source / 'app/src/main/AndroidManifest.xml').getroot()
    manifest_rows = []
    for node in manifest.findall('.//activity'):
        name = node.get(A+'name', '')
        full = 'com.dtsgt.mpos'+name if name.startswith('.') else name
        simple = full.split('.')[-1]
        manifest_rows.append({'class': full, 'name': simple, 'exported': node.get(A+'exported', 'default'),
                              'orientation': node.get(A+'screenOrientation'), 'configChanges': node.get(A+'configChanges'),
                              'launcher': any(x.get(A+'name') == 'android.intent.category.LAUNCHER' for x in node.findall('.//category')),
                              'domain': domain(simple), 'runtime': 'unobserved'})
    for file in sorted((source/'app/src/main/res').rglob('*.xml')):
        path = file.relative_to(source).as_posix()
        raw = file.read_bytes(); inventory.append({'file': path, 'sha256': sha(raw), 'bytes': len(raw), 'layer': '02-presentation'})
        try: xml = ET.fromstring(raw)
        except ET.ParseError:
            risks.append({'file': path, 'line': 1, 'pattern': 'xml_parse_gap', 'status': 'manual_review_required'}); continue
        context = xml.get(T+'context')
        # XML text is intentionally omitted; it can contain contact info or hardcoded customer labels.
        for node in xml.iter():
            if node.get(A+'onClick'):
                handlers.append({'file': path, 'layout': file.stem, 'context': context, 'view_id': node.get(A+'id'),
                                 'handler': node.get(A+'onClick'), 'runtime': 'unobserved'})
    # Hash build/manifest inputs without exporting their contents (which may contain private settings).
    for relative in ['app/src/main/AndroidManifest.xml','build.gradle','settings.gradle','app/build.gradle',
                     'gradle.properties','gradle/wrapper/gradle-wrapper.properties','gradle/gradle-daemon-jvm.properties']:
        file=source/relative
        if file.is_file():
            raw=file.read_bytes()
            inventory.append({'file':relative,'sha256':sha(raw),'bytes':len(raw),'layer':'09-platform-shared'})
    payloads = {'inventory': inventory, 'classes': classes, 'methods': methods, 'calls': calls, 'navigation': navigation,
                'layout_bindings': layouts, 'xml_handlers': handlers, 'global_state': globals_access,
                'sql_access': sql_access, 'schema_candidates': schema, 'risk_patterns': risks,
                'menu_items': menus, 'country_branches': country_sites, 'activities': manifest_rows}
    for name, rows in payloads.items(): write_rows(name, rows)
    commit = git(source, 'rev-parse', 'HEAD')
    status = git(source, 'status', '--porcelain')
    fingerprint = sha('\n'.join(r['file']+':'+r['sha256'] for r in inventory).encode())
    summary = {'schema': 1, 'generated_utc': datetime.now(timezone.utc).isoformat(), 'source_commit': commit,
               'source_branch': git(source, 'branch', '--show-current'), 'source_dirty_paths': status.splitlines(),
               'tracked_source_fingerprint': fingerprint, 'counts': {key: len(val) for key,val in payloads.items()},
               'java_parse_error_files': sum(r.get('parse_has_error',False) for r in inventory),
               'permissions': [n.get(A+'name') for n in manifest.findall('uses-permission')],
               'risk_counts': dict(Counter(r['pattern'] for r in risks)),
               'layers': dict(Counter(r['layer'] for r in classes)),
               'coverage_semantics': 'Static candidates; not observed runtime routes, resolved dispatch, proven defects or live DB schema.'}
    write_json(ROOT/'catalog/scan-summary.json',summary)
    # Only local configuration contains workstation paths; it is ignored by Git.
    write_json(ROOT/'.local/source.json',{'source': str(source), 'commit': commit})
    render(payloads,summary)
    print(json.dumps({'counts': summary['counts'], 'java_parse_error_files': summary['java_parse_error_files'], 'risk_counts': summary['risk_counts']},indent=2))


def render(data, summary):
    out=ROOT/'brain/generated'; out.mkdir(parents=True,exist_ok=True)
    text=['# Inventario estático generado','',f"Commit: `{summary['source_commit']}`.", '',
          'Estos índices describen candidatos del código; no acreditan recorrido ni permisos en ejecución.', '', '| Catálogo | Registros |','|---|---:|']
    text += [f'| {name} | {count} |' for name,count in summary['counts'].items()]
    (out/'inventory.md').write_text('\n'.join(text)+'\n',encoding='utf-8')
    for layer_name in sorted(summary['layers']):
        rows=[r for r in data['classes'] if r['layer']==layer_name]
        text=[f'# Capa {layer_name}','',f'Tipos inventariados: {len(rows)}. Estado: análisis estático.', '', '| Tipo | Archivo | Línea |','|---|---|---:|']
        text += [f"| `{r['class']}` | `{r['file']}` | {r['line']} |" for r in rows]
        (out/(layer_name+'.md')).write_text('\n'.join(text)+'\n',encoding='utf-8')
    flow_root=ROOT/'flows/activities'; flow_root.mkdir(parents=True,exist_ok=True)
    for activity in data['activities']:
        cls=activity['class']; simple=activity['name']
        types=[r for r in data['classes'] if r['class']==cls]
        ms=[r for r in data['methods'] if r['class']==cls]
        edges=[r for r in data['navigation'] if r['from_class']==cls]
        binds=[r for r in data['layout_bindings'] if r['class']==cls]
        gs=[r for r in data['global_state'] if r['class']==cls and r['access']=='write']
        text=[f'# {simple}','',f"Dominio: `{activity['domain']}`. Cobertura: **inventariado estático; no observado**.", '',
              '## Evidencia','',*[f"- `{r['file']}:{r['line']}`; hereda `{r['extends']}`." for r in types], '',
              '## Layouts candidatos','',*[f"- `{r['layout']}` — `{r['file']}:{r['line']}`." for r in binds], '',
              '## Navegación candidata','',*[f"- `{r['target']}` ({r['kind']}) — `{r['file']}:{r['line']}`; condiciones en catálogo." for r in edges], '',
              '## Estado global escrito','', ', '.join('`'+x+'`' for x in sorted({r['field'] for r in gs})) or 'No detectado.', '',
              '## Tablas mencionadas estáticamente','', ', '.join('`'+x+'`' for x in sorted({t for r in ms for t in r['tables']})) or 'No detectadas.', '',
              '## Métodos','',*[f"- `{r['name']}` — línea {r['line']}." for r in ms], '',
              '## Para acreditar aprendizaje operativo','', 'Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.']
        (flow_root/(simple+'.md')).write_text('\n'.join(text)+'\n',encoding='utf-8')
    index=['# Rutas por dominio','', 'Entradas generadas del manifiesto; rutas condicionadas deben validarse con fixtures.', '']
    for name in sorted({r['domain'] for r in data['activities']}):
        index += ['## '+name,'']+[f"- [{r['name']}](activities/{r['name']}.md)" for r in data['activities'] if r['domain']==name]+['']
    (ROOT/'flows/INDEX.md').write_text('\n'.join(index)+'\n',encoding='utf-8')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--source',type=Path,required=True)
    scan(p.parse_args().source)

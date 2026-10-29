"""Map literal P_PARAMEXT lookups to global writes in the same Java try; never export configuration values."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import subprocess
from tree_sitter import Language,Parser
import tree_sitter_java

ROOT=Path(__file__).resolve().parents[1]
RELATIVE='app/src/main/java/com/dtsgt/base/AppMethods.java'

def walk(node):
    yield node
    for child in node.named_children:yield from walk(child)

def nearest(node,kind):
    parent=node.parent
    while parent:
        if parent.type==kind:return parent
        parent=parent.parent

def extract(raw,relative=RELATIVE):
    parser=Parser(Language(tree_sitter_java.language()))
    tree=parser.parse(raw)
    if tree.root_node.has_error:raise ValueError('Java parse error; do not publish partial parameter map')
    text=lambda n:raw[n.start_byte:n.end_byte].decode('utf-8') if n else ''
    rows=[]
    for block in walk(tree.root_node):
        if block.type!='try_statement':continue
        ids=set()
        for node in walk(block.child_by_field_name('body')):
            if node.type=='string_literal' and nearest(node,'try_statement')==block:
                ids.update(int(m) for m in re.findall(r'\bP_PARAMEXT\b.*?\bID\s*=\s*(\d+)',text(node),re.I))
        if not ids:continue
        writes=[]
        for node in walk(block):
            if node.type!='assignment_expression' or nearest(node,'try_statement')!=block:continue
            lhs=node.child_by_field_name('left');rhs=node.child_by_field_name('right')
            if not lhs or lhs.type!='field_access' or text(lhs.child_by_field_name('object'))!='gl':continue
            field=text(lhs.child_by_field_name('field'))
            phase='catch' if nearest(node,'catch_clause') and nearest(nearest(node,'catch_clause'),'try_statement')==block else 'body'
            assignment={'global':field,'line':node.start_point.row+1,'phase':phase,'kind':'computed_or_reference'}
            literal=text(rhs)
            # Only boolean/numeric constants are exported; strings could be credentials or endpoints.
            if literal in ('true','false'):assignment.update(kind='boolean_literal',literal=literal=='true')
            elif re.fullmatch(r'-?\d+(?:\.\d+)?',literal):assignment.update(kind='numeric_literal',literal=float(literal) if '.' in literal else int(literal))
            elif re.fullmatch(r'val\.equalsIgnoreCase\("S"\)',literal):assignment['kind']='yes_no_S'
            writes.append(assignment)
        method=nearest(block,'method_declaration')
        rows.append({'file':relative,'line':block.start_point.row+1,'end_line':block.end_point.row+1,
                     'method':text(method.child_by_field_name('name')) if method else None,
                     'parameter_ids':sorted(ids),'global_writes':writes,
                     'binding':'same_try_candidate_not_full_dataflow','runtime':'unobserved'})
    return rows

def presence(rows,path):
    path=path.resolve()
    if not path.is_relative_to((ROOT/'.local').resolve()):raise ValueError('private snapshot must stay under .local')
    db=sqlite3.connect(path.as_uri()+'?mode=ro&immutable=1',uri=True)
    try:
        out=[]
        for param in sorted({i for row in rows for i in row['parameter_ids']}):
            count,variants=db.execute('SELECT COUNT(*),COUNT(DISTINCT VALOR) FROM P_PARAMEXT WHERE ID=?',(param,)).fetchone()
            out.append({'parameter_id':param,'row_count':count,'distinct_value_count':variants,
                        'status':'missing' if count==0 else 'conflicting_duplicates' if variants>1 else 'duplicate_rows' if count>1 else 'present'})
        return {'schema':1,'source':'private QA snapshot; no parameter values exported',
                'snapshot_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'parameters':out,
                'scope':'Presence is not evidence that a branch ran; defaults may have additional dependencies.'}
    finally:db.close()

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source',type=Path,required=True);p.add_argument('--database',type=Path);a=p.parse_args()
    raw=(a.source/RELATIVE).read_bytes();rows=extract(raw)
    target=ROOT/'catalog/config_params.jsonl'
    target.write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows),encoding='utf-8')
    metadata={'schema':1,'generated_utc':datetime.now(timezone.utc).isoformat(),
              'source_commit':subprocess.check_output(['git','-C',str(a.source),'rev-parse','HEAD']).decode().strip(),
              'file':RELATIVE,'source_sha256':hashlib.sha256(raw).hexdigest(),'lookup_blocks':len(rows),
              'parameter_ids':len({i for r in rows for i in r['parameter_ids']}),
              'scope':'Literal P_PARAMEXT lookups in AppMethods only; same-try writes, not complete dataflow or executed flags.'}
    (ROOT/'catalog/config-summary.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
    if a.database:(ROOT/'catalog/qa-config-presence.json').write_text(json.dumps(presence(rows,a.database),indent=2),encoding='utf-8')
    print(json.dumps({'lookup_blocks':metadata['lookup_blocks'],'parameter_ids':metadata['parameter_ids']}))

if __name__=='__main__':main()

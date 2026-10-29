"""Create private isolated clones and derive regression probes from real source blocks."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET
from tree_sitter import Language, Parser
import tree_sitter_java

ROOT=Path(__file__).resolve().parents[1]
VARIANTS={'guarded':'bd94c90c','rollback':'c21e92ec','qa':'bd94c90c'}
PARSER=Parser(Language(tree_sitter_java.language()))

def walk(n):
    yield n
    for c in n.named_children: yield from walk(c)

def replace_once(s,a,b):
    if s.count(a)!=1: raise ValueError('source drift at required anchor: '+a[:90])
    return s.replace(a,b,1)

def blocks(path):
    raw=path.read_bytes().removeprefix(b'\xef\xbb\xbf'); tree=PARSER.parse(raw)
    if tree.root_node.has_error: raise ValueError('cannot derive probes from unparsable source')
    text=lambda n:raw[n.start_byte:n.end_byte].decode('utf-8')
    ms={text(n.child_by_field_name('name')):n for n in walk(tree.root_node) if n.type=='method_declaration'}
    return ms,text

def derive_probe(workspace, variant):
    source=workspace/'app/src/main/java/com/dtsgt/mpos/FacturaRes.java'
    ms,text=blocks(source)
    origins=[]
    if variant=='qa':
        target=workspace/'app/src/brainTest/java/com/dtsgt/brainlabtests/QaBootstrapTest.java'
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text((ROOT/'experiments/onboarding/QaBootstrapTest.java.template').read_text(encoding='utf-8'),encoding='utf-8')
    def capture(node,label):
        code=text(node)
        origins.append({'fragment':label,'file':source.relative_to(workspace).as_posix(),'line':node.start_point.row+1,
                        'end_line':node.end_point.row+1,'sha256':hashlib.sha256(code.encode()).hexdigest()})
        return code
    create=ms['onCreate']
    assignment=next(n for n in walk(create) if n.type=='expression_statement' and re.sub(r'\s','',text(n))=='monto_propina=gl.pePropinaPerc;')
    following=assignment.next_named_sibling
    if following.type!='if_statement' or 'gl.propina_vacia' not in text(following): raise ValueError('initial tip omission anchor drift')
    init=capture(assignment,'initial_percentage')+'\n'+capture(following,'inherited_omit')
    ask=ms['askPropina']
    positive=next(n for n in walk(ask) if n.type=='method_invocation' and text(n.child_by_field_name('name'))=='setPositiveButton')
    lam=next(n for n in walk(positive) if n.type=='lambda_expression')
    choice=capture(lam.child_by_field_name('body'),'explicit_with_tip_callback')[1:-1]
    primary=ms['impresionCuenta']
    code=text(primary)
    if 'buildPrecuentaSafely' in ms:
        helper=capture(ms['buildPrecuentaSafely'],'guarded_document_gate')
        prepare=capture(ms['prepareExplicitTipPrint'],'guarded_explicit_choice')
        declaration=next(n for n in walk(primary) if n.type=='local_variable_declaration' and 'printValues = buildPrecuentaSafely' in text(n))
        check=declaration.next_named_sibling
        if check.type!='if_statement' or 'printValues == null' not in text(check): raise ValueError('dispatch check drift')
        call=next(n for n in walk(primary) if n.type=='expression_statement' and text(n).strip().startswith('app.doPrint('))
        dispatch=capture(declaration,'document_gate_call')+'\n'+capture(check,'document_gate_return')+'\n'+capture(call,'driver_dispatch')
        projection='com.dtsgt.diagnostics.PrecuentaValues v = com.dtsgt.diagnostics.PrecuentaValues.forPrint(tot,propina,propinaperc,Boolean.TRUE.equals(gl.pePropinaFija),omit); return new double[]{tot,propina,v.total,v.tip};'
        imports='import com.dtsgt.diagnostics.PrecuentaValues;'
    else:
        helper=prepare=imports=''
        mutation=next(n for n in walk(primary) if n.type=='if_statement' and re.sub(r'\s','',text(n.child_by_field_name('condition')))=='(propina_vacia)')
        projection='propina_vacia=omit;\n'+capture(mutation,'legacy_without_tip_mutation')+'\nreturn new double[]{tot,propina,tot,propina};'
        build=next(n for n in walk(primary) if n.type=='expression_statement' and text(n).strip().startswith('fdoc.buildPrint('))
        call=next(n for n in walk(primary) if n.type=='expression_statement' and text(n).strip().startswith('app.doPrint('))
        dispatch=capture(build,'unchecked_document_build')+'\n'+capture(call,'driver_dispatch')
    generated='''package com.dtsgt.brainlabtests;
import android.content.Context;
import android.content.ContextWrapper;
import com.dtsgt.base.appGlobals;
import com.dtsgt.classes.clsDocCuenta;
import com.dtsgt.diagnostics.DiagnosticLog;
__IMPORTS__
public class ExtractedTipProbe extends ContextWrapper {
 public appGlobals gl=new appGlobals();
 public double tot=148.5,propina=13.5,propinaperc=10,monto_propina=10,descimp=0,percentageAtPrint=-1;
 private boolean propina_vacia=false,EsNivelPrecioDelivery=false;
 private String diagnosticTraceId="brain-component-contract";
 public clsDocCuenta fdoc;
 public Driver app=new Driver();
 public Messages mu=new Messages();
 public ExtractedTipProbe(Context c){super(c);gl.codigo_pais="HN";gl.pePropinaFija=true;gl.peLlevarSinPropina=false;gl.pePropinaPerc=10;}
 public void initializeChoice(){__INIT__}
 public void confirmWithTip(){__CHOICE__}
 public double[] project(boolean omit){__PROJECT__}
 public void dispatch(){__DISPATCH__}
 private void tracePropina(String event){}
 private void totalOrder(){} // This probe validates percentage recovery, not a replacement for the production calculator.
 private void impresionCuenta(){percentageAtPrint=monto_propina;}
 public static class Messages {public void msgbox(String s){}}
 public static class Driver {
   public int calls; public java.io.File path;public String seen="";
   public void doPrint(int copies,int type,boolean cut){calls++;try{seen=new String(java.nio.file.Files.readAllBytes(path.toPath()),java.nio.charset.StandardCharsets.UTF_8);}catch(Exception ignored){}}
 }
 __HELPER__
 __PREPARE__
}
'''
    for key,value in {'IMPORTS':imports,'INIT':init,'CHOICE':choice,'PROJECT':projection,'DISPATCH':dispatch,'HELPER':helper,'PREPARE':prepare}.items():
        generated=generated.replace('__'+key+'__',value)
    dest=workspace/'app/src/brainTest/java/com/dtsgt/brainlabtests'
    dest.mkdir(parents=True,exist_ok=True)
    (dest/'ExtractedTipProbe.java').write_text(generated,encoding='utf-8')
    template=(ROOT/'experiments/propina/BrainTipContractTest.java.template').read_text(encoding='utf-8')
    (dest/'BrainTipContractTest.java').write_text(template.replace('__VARIANT__',variant),encoding='utf-8')
    return origins

def prepare(source, variant):
    workspace=(ROOT/'.local/workspaces'/variant).resolve()
    if not workspace.is_relative_to((ROOT/'.local/workspaces').resolve()): raise ValueError('unsafe lab path')
    if workspace.exists():
        raise ValueError('workspace exists; reuse it or explicitly archive it; never overwrite an experiment silently')
    workspace.parent.mkdir(parents=True,exist_ok=True)
    subprocess.run(['git','clone','--no-hardlinks','--quiet',str(source),str(workspace)],check=True)
    subprocess.run(['git','-C',str(workspace),'checkout','--quiet','--detach',VARIANTS[variant]],check=True)
    appid='com.dtsgt.mpos.brainqa' if variant=='qa' else 'com.dtsgt.mpos.brainlab'
    appgradle=workspace/'app/build.gradle'
    appgradle.write_text(appgradle.read_text(encoding='utf-8')+f'''
// Brain laboratory only. Not a production application or a source-repo change.
android {{
 defaultConfig {{ applicationId "{appid}"; testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner" }}
 sourceSets {{ androidTest.java.srcDirs = ['src/brainTest/java'] }}
}}
dependencies {{
 androidTestImplementation 'androidx.test:runner:1.7.0'
 androidTestImplementation 'androidx.test.ext:junit:1.3.0'
}}
''',encoding='utf-8')
    # Preserve private Firebase configuration inside ignored clones; change only the lab package mapping.
    gpath=workspace/'app/google-services.json'
    config=json.loads(gpath.read_text(encoding='utf-8'))
    for client in config.get('client',[]):
        client['client_info']['android_client_info']['package_name']=appid
    gpath.write_text(json.dumps(config),encoding='utf-8')
    path=workspace/'app/src/main/AndroidManifest.xml'
    manifest=path.read_text(encoding='utf-8')
    if variant!='qa':
        manifest=replace_once(manifest,'<uses-permission android:name="android.permission.INTERNET" />',
                              '<uses-permission android:name="android.permission.INTERNET" tools:node="remove" />')
    manifest=replace_once(manifest,'<application','<application')
    for item in ['firebase_analytics_collection_enabled','firebase_crashlytics_collection_enabled','firebase_performance_collection_enabled']:
        manifest=manifest.replace('</application>',f'<meta-data android:name="{item}" android:value="false" />\n</application>')
    # SDK installation registration otherwise attempts network even when collection is disabled.
    manifest=manifest.replace('</application>','<provider android:name="com.google.firebase.provider.FirebaseInitProvider" android:authorities="${applicationId}.firebaseinitprovider" tools:node="remove" />\n</application>')
    path.write_text(manifest,encoding='utf-8')
    (workspace/'local.properties').write_text('sdk.dir=C:/Users/yejc2/AppData/Local/Android/Sdk\n',encoding='utf-8')
    (workspace/'.gradle').mkdir(exist_ok=True)
    (workspace/'.gradle/config.properties').write_text('java.home=C:/Program Files/Microsoft/jdk-17.0.20.101-hotspot\n',encoding='utf-8')
    origins=[]
    if variant!='qa':
        document=workspace/'app/src/main/java/com/dtsgt/classes/clsDocument.java'
        doc=document.read_text(encoding='utf-8')
        doc=replace_once(doc,'private boolean buildHeader()','protected boolean buildHeader()')
        document.write_text(doc,encoding='utf-8')
        origins=derive_probe(workspace,variant)
    provenance={'variant':variant,'commit':subprocess.check_output(['git','-C',str(workspace),'rev-parse','HEAD']).decode().strip(),
                'application_id':appid,'network_permission':variant=='qa','test_seams':(['private buildHeader() made protected in lab only; DB header stubbed','physical printer replaced by a recording driver','percentage recovery probe does not execute the calculator'] if variant!='qa' else ['actual MainActivity and WSRec with payload-free phase observer']),
                'source_fragments':origins,'source_repo_modified':False,
                'firebase_initialization':'FirebaseInitProvider removed in lab manifest; no SDK installation registration'}
    (workspace/'brain-lab-provenance.json').write_text(json.dumps(provenance,indent=2),encoding='utf-8')
    if variant=='qa':
        from qa_trace import install
        install()
    print(json.dumps({'workspace':str(workspace),'variant':variant,'application_id':appid,'fragments':len(origins)}))
    return workspace

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source',type=Path,required=True);p.add_argument('--variant',choices=VARIANTS,required=True)
    args=p.parse_args();prepare(args.source.resolve(),args.variant)

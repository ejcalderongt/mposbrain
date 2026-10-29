"""Install payload-free phase observers exclusively in the private QA laboratory clone."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def install():
    workspace=ROOT/'.local/workspaces/qa'
    provenance=json.loads((workspace/'brain-lab-provenance.json').read_text())
    if provenance['application_id']!='com.dtsgt.mpos.brainqa':raise ValueError('QA clone required')
    path=workspace/'app/src/main/java/com/dtsgt/mpos/WSRec.java'
    source=path.read_text(encoding='utf-8')
    if 'void brainQaTrace(' in source:return
    replacements={
        'private void execws(int callbackvalue) {':'private void execws(int callbackvalue) {\n brainQaTrace("callback",callbackvalue);',
        'private void processData() {':'private void processData() {\n brainQaTrace("base_transaction_enter",0);',
        'gl.estado_recep=true;':'gl.estado_recep=true;\n brainQaTrace("base_transaction_committed",0);',
        'private void processDataFinal() {':'private void processDataFinal() {\n brainQaTrace("final_enter",0);',
        'limpiaArchivosCierre();':'limpiaArchivosCierre();\n brainQaTrace("final_validations_returned",0);',
    }
    for before,after in replacements.items():
        if source.count(before)!=1:raise ValueError('source drift at phase observer anchor')
        source=source.replace(before,after,1)
    method='''
    // Brain QA observer only: phase identifiers/numbers, never payloads or widget values.
    private synchronized void brainQaTrace(String stage,int number) {
        try(java.io.FileOutputStream f=new java.io.FileOutputStream(new java.io.File(getCacheDir(),"brain-sync-phase.jsonl"),true)) {
            org.json.JSONObject row=new org.json.JSONObject();row.put("stage",stage);row.put("number",number);
            f.write((row.toString()+"\\n").getBytes(java.nio.charset.StandardCharsets.UTF_8));
        } catch(Exception ignored) { }
    }
'''
    pos=source.rfind('}')
    path.write_text(source[:pos]+method+source[pos:],encoding='utf-8')
    provenance['qa_observers']='WSRec callback number and phase-only observer; no payloads; final marker means validations returned, not all postconditions asserted'
    (workspace/'brain-lab-provenance.json').write_text(json.dumps(provenance,indent=2),encoding='utf-8')

if __name__=='__main__':install()

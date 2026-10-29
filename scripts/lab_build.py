"""Build an existing isolated laboratory clone, never the user's active checkout."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import time

ROOT=Path(__file__).resolve().parents[1]

def build(variant):
    workspace=(ROOT/'.local/workspaces'/variant).resolve()
    if not workspace.is_relative_to((ROOT/'.local/workspaces').resolve()): raise ValueError('unsafe workspace')
    provenance=json.loads((workspace/'brain-lab-provenance.json').read_text())
    if provenance['variant']!=variant: raise ValueError('variant mismatch')
    output=ROOT/'.local/builds';output.mkdir(parents=True,exist_ok=True)
    log=output/(variant+'.txt')
    env=os.environ.copy();env['JAVA_HOME']='C:/Program Files/Microsoft/jdk-17.0.20.101-hotspot'
    tasks=[':app:assembleDebug',':app:assembleDebugAndroidTest']
    start=time.monotonic()
    with log.open('w',encoding='utf-8') as file:
        completed=subprocess.run([str(workspace/'gradlew.bat'),*tasks,'--console=plain','--max-workers=4'],cwd=workspace,env=env,stdout=file,stderr=subprocess.STDOUT,timeout=1200)
    summary={'variant':variant,'exit_code':completed.returncode,'seconds':round(time.monotonic()-start,2),'source_commit':provenance['commit'],'log_private':True}
    (output/(variant+'-result.json')).write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps(summary),flush=True)
    if completed.returncode: raise SystemExit(completed.returncode)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--variant',choices=['guarded','rollback','qa','flow-guarded','flow-rollback'],required=True);build(p.parse_args().variant)

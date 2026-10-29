"""Observe authorized first receive on a dedicated, initially empty QA AVD. Private fixture is never printed."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import subprocess
import time
import sqlite3

ROOT=Path(__file__).resolve().parents[1]
ADB=Path('C:/Users/yejc2/AppData/Local/Android/Sdk/platform-tools/adb.exe')

def run(serial,resume_empty=False):
    def adb(*args,timeout=90):
        return subprocess.run([str(ADB),'-s',serial,*args],capture_output=True,timeout=timeout)
    name=adb('emu','avd','name',timeout=15).stdout.decode('utf-8','replace')
    if 'mPos_Brain_QA_10' not in name:raise ValueError('requires dedicated QA AVD')
    deadline=time.monotonic()+180
    while adb('shell','getprop','sys.boot_completed',timeout=15).stdout.strip()!=b'1':
        if time.monotonic()>deadline:raise RuntimeError('QA Android boot did not finish; app has not been tested')
        time.sleep(3)
    workspace=ROOT/'.local/workspaces/qa';package='com.dtsgt.mpos.brainqa'
    private=ROOT/'.local/results/qa';private.mkdir(parents=True,exist_ok=True)
    if adb('shell','test','-f','/sdcard/posdts.db').returncode==0:
        if not resume_empty:raise ValueError('QA database already exists; preserve it and inspect before any new bootstrap')
        adb('shell','am','force-stop',package)
        snapshot=private/('resume-empty-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')+'.db')
        if adb('pull','/sdcard/posdts.db',str(snapshot)).returncode:raise RuntimeError('cannot preserve existing QA database')
        db=sqlite3.connect(snapshot.as_uri()+'?mode=ro',uri=True)
        try:
            if db.execute('PRAGMA quick_check').fetchone()[0]!='ok':raise ValueError('inconsistent existing QA snapshot')
            for table in ['P_EMPRESA','P_RUTA','P_SUCURSAL','T_VENTA','T_PAGO']:
                if db.execute('SELECT COUNT(*) FROM '+table).fetchone()[0]:raise ValueError('existing QA base is not empty: preserve and inspect without bootstrap')
        finally:db.close()
    for number,path in enumerate([workspace/'app/build/outputs/apk/debug/app-debug.apk',workspace/'app/build/outputs/apk/androidTest/debug/app-debug-androidTest.apk']):
        result=adb('install','-r','-g',str(path))
        (private/('install-'+str(number)+'.txt')).write_bytes(result.stdout+result.stderr)
        if result.returncode:raise RuntimeError('QA install failed; inspect local device')
    fixture=ROOT/'.local/qa-input.json'
    if not fixture.is_file():raise ValueError('private QA fixture missing')
    remote='/sdcard/Download/brain-qa-input.json'
    if adb('push',str(fixture),remote).returncode:raise RuntimeError('private fixture transfer failed')
    try:
        result=adb('shell','am','instrument','-w','-r','-e','class','com.dtsgt.brainlabtests.QaBootstrapTest',package+'.test/androidx.test.runner.AndroidJUnitRunner',timeout=390)
        (private/'instrumentation.txt').write_bytes(result.stdout+result.stderr)
        observations=adb('exec-out','run-as',package,'cat','cache/brain-onboarding.jsonl')
        (private/'observations.jsonl').write_bytes(observations.stdout)
        if not observations.stdout.lstrip().startswith(b'{'):
            raise RuntimeError('QA observer did not start; inspect private instrumentation and Android exit-info; not an application-flow result')
        rows=[json.loads(line) for line in observations.stdout.decode('utf-8').splitlines() if line.strip()]
        phases=adb('exec-out','run-as',package,'cat','cache/brain-sync-phase.jsonl').stdout
        (private/'phases.jsonl').write_bytes(phases)
        phase_rows=[json.loads(line) for line in phases.decode('utf-8').splitlines() if line.lstrip().startswith('{')]
        if any(set(row)!={'stage','number'} for row in phase_rows):raise RuntimeError('unsafe phase observation')
        # Output was designed as a structure-only allowlist; verify before publishing.
        allowed={'stage','received','activity','nodes'};node_allowed={'id','type','visible','enabled','bounds'}
        if not rows or any(set(row)-allowed or any(set(n)-node_allowed for n in row['nodes']) for row in rows):
            raise RuntimeError('missing or unsafe QA structural observation')
        provenance=json.loads((workspace/'brain-lab-provenance.json').read_text())
        output={'schema':1,'time_utc':datetime.now(timezone.utc).isoformat(),'source_commit':provenance['commit'],
                'sdk':int(adb('shell','getprop','ro.build.version.sdk').stdout.strip()),
                'avd':name.strip().splitlines()[0],
                'apk_sha256':hashlib.sha256((workspace/'app/build/outputs/apk/debug/app-debug.apk').read_bytes()).hexdigest(),
                'observers':provenance.get('qa_observers','phase-only observer'),
                'kind':'Actual Android Activity startup and authorized QA receive; no sales or sends',
                'base_transaction_received':rows[-1]['received'],
                'final_validations_returned':any(r['stage']=='final_validations_returned' for r in phase_rows),
                'received':rows[-1]['received'] and any(r['stage']=='final_validations_returned' for r in phase_rows),
                'phases':phase_rows,'events':rows}
        out=ROOT/'evidence/onboarding';out.mkdir(parents=True,exist_ok=True)
        (out/'qa-bootstrap.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
        print(json.dumps({'received':output['received'],'observed_stages':[r['stage'] for r in rows],'activities':[r['activity'] for r in rows]}))
    finally:
        adb('shell','rm','-f',remote,timeout=20)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--serial',default='emulator-5584');p.add_argument('--resume-empty',action='store_true');a=p.parse_args();run(a.serial,a.resume_empty)

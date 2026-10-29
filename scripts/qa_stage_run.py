"""Run authorized second/third QA receives without resetting the database or emitting sales."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import sqlite3
import subprocess
from db_index import describe
from lab_run import parse_status

ROOT=Path(__file__).resolve().parents[1]
ADB=Path('C:/Users/yejc2/AppData/Local/Android/Sdk/platform-tools/adb.exe')

def run(stage,serial):
    def adb(*args,timeout=90):return subprocess.run([str(ADB),'-s',serial,*args],capture_output=True,timeout=timeout)
    avd=adb('emu','avd','name',timeout=15).stdout.decode().splitlines()[0]
    if not avd.startswith('mPos_Brain_QA_10'):raise ValueError('dedicated QA AVD required')
    if adb('shell','getprop','sys.boot_completed').stdout.strip()!=b'1':raise ValueError('Android not ready')
    attempt=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')
    package='com.dtsgt.mpos.brainqa';private=ROOT/'.local/results'/('qa-stage'+str(stage))/attempt;private.mkdir(parents=True,exist_ok=True)
    adb('shell','am','force-stop',package)
    before=private/('before-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')+'.db')
    if adb('pull','/sdcard/posdts.db',str(before)).returncode:raise RuntimeError('cannot preserve QA base')
    profile=json.loads((ROOT/'.local/qa-profile.json').read_text())
    db=sqlite3.connect(before.as_uri()+'?mode=ro',uri=True)
    try:
        if db.execute('PRAGMA quick_check').fetchone()[0]!='ok':raise ValueError('QA snapshot invalid')
        if db.execute('SELECT COUNT(*) FROM P_EMPRESA').fetchone()[0]!=1:raise ValueError('initial company receive missing')
        for table in ['D_FACTURA','T_VENTA','T_PAGO']:
            if db.execute('SELECT COUNT(*) FROM '+table).fetchone()[0]:raise ValueError('QA base contains operational documents; inspect before proceeding')
        if stage==3:
            if db.execute("SELECT COUNT(*) FROM P_PARAMEXT WHERE ID=118 AND UPPER(VALOR)='S'").fetchone()[0]!=1:raise ValueError('second receive has not enabled restaurant')
            if db.execute('SELECT COUNT(*) FROM Params WHERE SUCURSAL=? AND RUTA=?',(profile['store'],profile['route'])).fetchone()[0]!=1:raise ValueError('authorized profile not configured')
    finally:db.close()
    workspace=ROOT/'.local/workspaces/qa'
    for path in [workspace/'app/build/outputs/apk/debug/app-debug.apk',workspace/'app/build/outputs/apk/androidTest/debug/app-debug-androidTest.apk']:
        target_package=package+'.test' if 'androidTest' in str(path) else package
        locations=adb('shell','pm','path',target_package).stdout.decode('utf-8','replace').splitlines()
        if len(locations)==1 and locations[0].startswith('package:'):
            current=adb('shell','sha256sum',locations[0].split(':',1)[1]).stdout.decode('utf-8','replace').split()
            if current and current[0]==hashlib.sha256(path.read_bytes()).hexdigest():continue
        result=adb('install','-r','-g',str(path))
        if result.returncode:raise RuntimeError('stage APK install failed')
    adb('shell','run-as',package,'rm','-f','cache/brain-sync-phase.jsonl','cache/brain-onboarding.jsonl','cache/brain-stage-state.jsonl','cache/brain-private-dialogs.txt')
    remotes=[]
    try:
        for local,remote in [('qa-input.json','/sdcard/Download/brain-qa-input.json'),('qa-profile.json','/sdcard/Download/brain-qa-profile.json')]:
            if adb('push',str(ROOT/'.local'/local),remote).returncode:raise RuntimeError('private fixture transfer failed')
            remotes.append(remote)
        result=adb('shell','am','instrument','-w','-r','-e','stage',str(stage),'-e','class','com.dtsgt.brainlabtests.QaStagedReceiveTest',package+'.test/androidx.test.runner.AndroidJUnitRunner',timeout=440)
        raw=(result.stdout+result.stderr).decode('utf-8','replace');(private/'instrumentation.txt').write_text(raw,encoding='utf-8')
        (private/'dialogs-private.txt').write_bytes(adb('exec-out','run-as',package,'cat','cache/brain-private-dialogs.txt').stdout)
        groups={}
        for key,file in [('events','brain-onboarding.jsonl'),('phases','brain-sync-phase.jsonl'),('states','brain-stage-state.jsonl')]:
            data=adb('exec-out','run-as',package,'cat','cache/'+file).stdout
            (private/file).write_bytes(data)
            groups[key]=[json.loads(line) for line in data.decode('utf-8','replace').splitlines() if line.lstrip().startswith('{')]
        allowed_state={'stage','moment','countryHN','restaurantMode','storeMatchesAuthorized','routeMatchesAuthorized','restaurantParameterEnabled','rooms','tables'}
        if any(set(row)-allowed_state for row in groups['states']):raise ValueError('unexpected state fields')
        for event in groups['events']:
            if set(event)-{'stage','received','activity','nodes'} or any(set(n)-{'id','type','visible','enabled','bounds'} for n in event['nodes']):raise ValueError('unexpected structural UI fields')
        if any(set(row)-{'stage','number'} for row in groups['phases']):raise ValueError('unexpected phase fields')
        statuses=parse_status(raw)
        out={'schema':1,'stage_number':stage,'attempt_id':attempt,'time_utc':datetime.now(timezone.utc).isoformat(),'source_commit':json.loads((workspace/'brain-lab-provenance.json').read_text())['commit'],
             'sdk':int(adb('shell','getprop','ro.build.version.sdk').stdout.strip()),'avd':avd,
             'apk_sha256':hashlib.sha256((workspace/'app/build/outputs/apk/debug/app-debug.apk').read_bytes()).hexdigest(),
             'test_apk_sha256':hashlib.sha256((workspace/'app/build/outputs/apk/androidTest/debug/app-debug-androidTest.apk').read_bytes()).hexdigest(),
             'test_source_sha256':hashlib.sha256((workspace/'app/src/brainTest/java/com/dtsgt/brainlabtests/QaStagedReceiveTest.java').read_bytes()).hexdigest(),
             'statuses':statuses,'kind':'Actual ConfigCaja controls and WSRec receive; test harness enters activities directly; login/menu permissions not covered',**groups}
        public=ROOT/'evidence/onboarding'/('qa-stage'+str(stage)+'-attempt-'+attempt+'.json');public.write_text(json.dumps(out,indent=2),encoding='utf-8')
        if statuses=={'configuredRouteReceivesNextStage':'pass'}:
            (public.parent/('qa-stage'+str(stage)+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
        adb('shell','am','force-stop',package)
        if any(adb('shell','test','-s','/sdcard/posdts.db'+suffix).returncode==0 for suffix in ['-wal','-journal']):raise RuntimeError('pending SQLite sidecar; do not export inconsistent schema')
        after=ROOT/'.local/fixtures'/('qa-after-stage'+str(stage)+'-'+attempt+'.db')
        if after.exists():raise ValueError('stage snapshot already exists; preserve before a repeat')
        if adb('pull','/sdcard/posdts.db',str(after)).returncode:raise RuntimeError('cannot snapshot stage result')
        schema=describe(after)
        if statuses=={'configuredRouteReceivesNextStage':'pass'}:
            (ROOT/'catalog'/('runtime-qa-stage'+str(stage)+'-schema.json')).write_text(json.dumps(schema,indent=2),encoding='utf-8')
        print(json.dumps({'stage':stage,'statuses':statuses,'states':groups['states'],'ui_fingerprints':len(groups['events'])},indent=2))
        if statuses!={'configuredRouteReceivesNextStage':'pass'}:raise RuntimeError('stage assertion failed; inspect private evidence')
    finally:
        for remote in remotes:adb('shell','rm','-f',remote,timeout=20)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--stage',type=int,choices=[2,3],required=True);p.add_argument('--serial',default='emulator-5584');a=p.parse_args();run(a.stage,a.serial)

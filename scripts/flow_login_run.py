"""Exercise an authorized operator through real login controls in the isolated flow laboratory."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import sqlite3
import subprocess
from flow_fixture import verify_gate
from lab_run import parse_status

ROOT=Path(__file__).resolve().parents[1]
ADB=Path('C:/Users/yejc2/AppData/Local/Android/Sdk/platform-tools/adb.exe')

def run(role,variant,serial):
    adb=verify_gate(serial,variant);package='com.dtsgt.mpos.brainflow'
    attempt=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S');private=ROOT/'.local/results/flow-login'/role/attempt;private.mkdir(parents=True,exist_ok=True)
    operator=json.loads((ROOT/'.local/qa-selected-operators.json').read_text())[role]
    # The whole selected row stays private. Only this test's operator is transferred temporarily.
    fixture=private/'operator.json';fixture.write_text(json.dumps(operator),encoding='utf-8')
    workspace=ROOT/'.local/workspaces'/variant
    if adb('install','-r','-g',str(workspace/'app/build/outputs/apk/androidTest/debug/app-debug-androidTest.apk')).returncode:raise RuntimeError('flow login test install failed')
    adb('shell','am','force-stop',package)
    adb('shell','run-as',package,'rm','-f','cache/brain-onboarding.jsonl','cache/brain-login-result.json','cache/brain-login-private-dialog.txt')
    remote='/sdcard/Download/brain-operator.json'
    if adb('push',str(fixture),remote).returncode:raise RuntimeError('private operator transfer failed')
    try:
        completed=subprocess.run([str(ADB),'-s',serial,'shell','am','instrument','-w','-r','-e','role',role,'-e','class','com.dtsgt.brainlabtests.FlowLoginTest',package+'.test/androidx.test.runner.AndroidJUnitRunner'],capture_output=True,timeout=120)
        raw=(completed.stdout+completed.stderr).decode('utf-8','replace');(private/'instrumentation.txt').write_text(raw,encoding='utf-8')
        observation=adb('exec-out','run-as',package,'cat','cache/brain-login-result.json').stdout
        (private/'result.json').write_bytes(observation)
        (private/'dialogs-private.txt').write_bytes(adb('exec-out','run-as',package,'cat','cache/brain-login-private-dialog.txt').stdout)
        raw_events=adb('exec-out','run-as',package,'cat','cache/brain-onboarding.jsonl').stdout;(private/'events.jsonl').write_bytes(raw_events)
        events=[json.loads(line) for line in raw_events.decode('utf-8','replace').splitlines() if line.lstrip().startswith('{')]
        if not observation.lstrip().startswith(b'{'):raise RuntimeError('login observation unavailable; inspect private output')
        result=json.loads(observation)
        if set(result)-{'role','landedOnMenu','selectedVendorMatches','routeMatches','runtimeRole','restaurantMode','countryHN','menuItemIds'}:raise ValueError('unexpected login fields')
        for event in events:
            if set(event)-{'stage','received','activity','nodes'} or any(set(n)-{'id','type','visible','enabled','bounds'} for n in event['nodes']):raise ValueError('unexpected UI fields')
        statuses=parse_status(raw)
        out={'schema':1,'time_utc':datetime.now(timezone.utc).isoformat(),'attempt_id':attempt,'variant':variant,
             'source_commit':json.loads((workspace/'brain-lab-provenance.json').read_text())['commit'],
             'apk_sha256':hashlib.sha256((workspace/'app/build/outputs/apk/debug/app-debug.apk').read_bytes()).hexdigest(),
             'test_source_sha256':hashlib.sha256((workspace/'app/src/brainFlowTest/java/com/dtsgt/brainlabtests/FlowLoginTest.java').read_bytes()).hexdigest(),
             'network_gate_checked_before_run':True,'statuses':statuses,'result':result,'events':events,
             'scope':'Real user selection and keypad; isolated database/profile copy; no sales/payment/close controls exercised'}
        public=ROOT/'evidence/auth';public.mkdir(exist_ok=True)
        (public/(role+'-attempt-'+attempt+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
        if statuses=={'authorizedOperatorLogsInThroughControls':'pass'}:(public/(role+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
        print(json.dumps({'role':role,'statuses':statuses,'result':result,'ui_fingerprints':len(events)},indent=2))
        if statuses!={'authorizedOperatorLogsInThroughControls':'pass'}:raise RuntimeError('operator login failed; inspect private feedback')
    finally:
        adb('shell','am','force-stop',package);adb('shell','rm','-f',remote)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--role',choices=['waiter','cashier','manager'],required=True);p.add_argument('--variant',choices=['flow-guarded','flow-rollback'],default='flow-guarded');p.add_argument('--serial',default='emulator-5586');a=p.parse_args();run(a.role,a.variant,a.serial)

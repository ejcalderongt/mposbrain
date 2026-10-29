"""Run Android component contracts on the dedicated lab AVD; retain raw evidence privately."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time

ROOT=Path(__file__).resolve().parents[1]
ADB=Path('C:/Users/yejc2/AppData/Local/Android/Sdk/platform-tools/adb.exe')
AAPT=Path('C:/Users/yejc2/AppData/Local/Android/Sdk/build-tools/35.0.0/aapt.exe')

def adb(serial,*args,**kw):
    return subprocess.run([str(ADB),'-s',serial,*args],capture_output=True,**kw)

def parse_status(text):
    current=None; results={}
    for line in text.splitlines():
        if line.startswith('INSTRUMENTATION_STATUS: test='):current=line.split('=',1)[1]
        if line.startswith('INSTRUMENTATION_STATUS_CODE:') and current:
            code=int(line.split(':',1)[1].strip())
            if code in (0,-1,-2,-3,-4):results[current]={0:'pass',-1:'error',-2:'fail',-3:'ignored',-4:'assumption_failed'}[code]
    return results

def run(variant,serial):
    workspace=ROOT/'.local/workspaces'/variant
    provenance=json.loads((workspace/'brain-lab-provenance.json').read_text())
    package=provenance['application_id']
    if package!='com.dtsgt.mpos.brainlab' or provenance['network_permission']: raise ValueError('not an offline regression variant')
    avd=adb(serial,'emu','avd','name',timeout=15).stdout.decode('utf-8','replace')
    if 'mPos_Brain_Lab_10' not in avd: raise ValueError('refusing to install/clear anything outside the dedicated lab AVD')
    apk=workspace/'app/build/outputs/apk/debug/app-debug.apk'
    test_apk=workspace/'app/build/outputs/apk/androidTest/debug/app-debug-androidTest.apk'
    permissions=subprocess.check_output([str(AAPT),'dump','permissions',str(apk)]).decode('utf-8','replace')
    if 'android.permission.INTERNET' in permissions: raise ValueError('offline laboratory APK unexpectedly has INTERNET permission')
    start=time.monotonic()
    for args in [('install','-r','-g',str(apk)),('install','-r',str(test_apk)),('shell','pm','clear',package)]:
        result=adb(serial,*args,timeout=90)
        if result.returncode or ('Success' not in result.stdout.decode('utf-8','replace')):raise RuntimeError('lab install/clear failed; inspect private device state')
    result=adb(serial,'shell','am','instrument','-w','-r','-e','class','com.dtsgt.brainlabtests.BrainTipContractTest',package+'.test/androidx.test.runner.AndroidJUnitRunner',timeout=240)
    raw=result.stdout.decode('utf-8','replace')+result.stderr.decode('utf-8','replace')
    private=ROOT/'.local/results'/variant;private.mkdir(parents=True,exist_ok=True)
    (private/'instrumentation.txt').write_text(raw,encoding='utf-8')
    observations=adb(serial,'exec-out','run-as',package,'cat','cache/brain-observations.jsonl',timeout=30)
    if observations.returncode or not observations.stdout.lstrip().startswith(b'{'):
        raise RuntimeError('instrumentation observations unavailable; infrastructure failure, not a reproduced defect; see private output')
    (private/'observations.jsonl').write_bytes(observations.stdout)
    rows=[json.loads(line) for line in observations.stdout.decode('utf-8').splitlines() if line.strip()]
    statuses=parse_status(raw)
    summary={'schema':1,'variant':variant,'source_commit':provenance['commit'],'time_utc':datetime.now(timezone.utc).isoformat(),
             'experiment_kind':'Android component contracts; extracted source probes + production receipt generator + injected failures',
             'country_fixture':'HN','dedicated_avd':True,'network_permission':False,
             'apk_sha256':hashlib.sha256(apk.read_bytes()).hexdigest(),'duration_seconds':round(time.monotonic()-start,2),
             'statuses':statuses,'observations':rows,'source_fragments':provenance['source_fragments'],'test_seams':provenance['test_seams']}
    public=ROOT/'evidence/experiments';public.mkdir(parents=True,exist_ok=True)
    (public/(variant+'.json')).write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps({'variant':variant,'statuses':statuses,'observations':len(rows)},indent=2))
    if len(statuses)!=7 or len(rows)!=7:raise RuntimeError('incomplete experiment: expected seven component contracts and observations')
    return summary

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--variant',choices=['guarded','rollback'],required=True);p.add_argument('--serial',default='emulator-5580')
    a=p.parse_args();run(a.variant,a.serial)

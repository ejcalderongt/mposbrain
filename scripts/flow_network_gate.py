"""Gate the dedicated flow AVD: demo Firebase SDK, local round trip and blocked guest-app egress."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import urllib.parse
import urllib.request
from lab_run import parse_status

ROOT=Path(__file__).resolve().parents[1]
ADB=Path('C:/Users/yejc2/AppData/Local/Android/Sdk/platform-tools/adb.exe')
CHAIN='MPOS_BRAIN_FLOW'
UID_RANGE='10000-199999'

def run(variant,serial,verify_only=False):
    def adb(*args,timeout=90):return subprocess.run([str(ADB),'-s',serial,*args],capture_output=True,timeout=timeout)
    name=adb('emu','avd','name',timeout=15).stdout.decode('utf-8','replace').splitlines()[0]
    if name!='mPos_Brain_Flow_10_API35':raise ValueError('network policy allowed only on dedicated flow AVD')
    if adb('shell','getprop','sys.boot_completed').stdout.strip()!=b'1':raise ValueError('flow Android is not booted')
    workspace=ROOT/'.local/workspaces'/variant
    provenance=json.loads((workspace/'brain-lab-provenance.json').read_text())
    package=provenance['application_id']
    if package!='com.dtsgt.mpos.brainflow' or provenance['firebase_project']!='demo-mpos-brain':raise ValueError('not a demo flow laboratory')
    adb('root');adb('wait-for-device')
    if adb('shell','id','-u').stdout.strip()!=b'0':raise RuntimeError('guest root required for verified egress policy')
    hub=json.load(urllib.request.urlopen('http://127.0.0.1:19440/emulators',timeout=5))
    if hub.get('database',{}).get('host')!='127.0.0.1' or hub['database'].get('port')!=19000:raise ValueError('dedicated database emulator not ready')
    attempt=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S');private=ROOT/'.local/results/flow-network'/attempt;private.mkdir(parents=True,exist_ok=True)
    for relative in ['app/build/outputs/apk/debug/app-debug.apk','app/build/outputs/apk/androidTest/debug/app-debug-androidTest.apk']:
        result=adb('install','-r','-g',str(workspace/relative))
        if result.returncode:raise RuntimeError('flow APK install failed; business writes remain forbidden')
    if adb('reverse','tcp:19000','tcp:19000').returncode:raise RuntimeError('ADB local tunnel failed')
    endpoint=urllib.parse.urlparse(str(json.loads((ROOT/'.local/qa-input.json').read_text())['endpoint']))
    target=private/'gate-target.json';target.write_text(json.dumps({'host':endpoint.hostname,'port':endpoint.port or (443 if endpoint.scheme=='https' else 80)}))
    remote='/sdcard/Download/brain-gate-target.json'
    if adb('push',str(target),remote).returncode:raise RuntimeError('gate target transfer failed')
    observations=[];statuses={}
    def instrument(phase):
        result=adb('shell','am','instrument','-w','-r','-e','phase',phase,'-e','class','com.dtsgt.brainlabtests.NetworkGateTest',package+'.test/androidx.test.runner.AndroidJUnitRunner',timeout=120)
        raw=(result.stdout+result.stderr).decode('utf-8','replace');(private/(phase+'-instrumentation.txt')).write_text(raw,encoding='utf-8')
        status=parse_status(raw);statuses[phase]=status
        data=adb('exec-out','run-as',package,'cat','cache/brain-network-gate.json').stdout
        if not data.lstrip().startswith(b'{'):raise RuntimeError('network gate produced no observation')
        row=json.loads(data);allowed={'schema','phase','demoProject','externalConnectSucceeded','localSdkRoundTrip','probeRemoved'}
        if set(row)-allowed or row.get('phase')!=phase:raise ValueError('unsafe or stale gate observation')
        observations.append(row)
        if status!={'verifyNetworkBoundary':'pass'}:raise RuntimeError('network boundary test failed; no business writes permitted')
    try:
        if not verify_only:
            for family in ['iptables','ip6tables']:
                if adb('shell',family,'-w','-S',CHAIN).returncode==0:raise ValueError('existing lab network chain: use --verify-only; never flush uninspected rules')
            instrument('baseline') # TCP connect/close only; no credentials, HTTP body or business data.
            for family,loopback in [('iptables','127.0.0.0/8'),('ip6tables','::1/128')]:
                for args in [('-N',CHAIN),('-A',CHAIN,'-d',loopback,'-j','RETURN'),('-A',CHAIN,'-j','REJECT'),('-I','OUTPUT','1','-m','owner','--uid-owner',UID_RANGE,'-j',CHAIN)]:
                    if adb('shell',family,'-w',*args).returncode:raise RuntimeError('partial guest-app policy; leave app stopped and inspect; gate not approved')
        policies={}
        for family,loopback in [('iptables','127.0.0.0/8'),('ip6tables','::1/128')]:
            hook=adb('shell',family,'-w','-S','OUTPUT').stdout.decode('utf-8','replace')
            rules=adb('shell',family,'-w','-S',CHAIN).stdout.decode('utf-8','replace')
            (private/(family+'-policy.txt')).write_text(hook+'\n'+rules,encoding='utf-8')
            if not any('--uid-owner '+UID_RANGE in line and '-j '+CHAIN in line for line in hook.splitlines()):raise ValueError('guest-app policy hook missing')
            if loopback not in rules or '-j RETURN' not in rules or '-j REJECT' not in rules:raise ValueError('loopback/reject policy incomplete')
            policies[family]={'guest_app_uid_range':UID_RANGE,'loopback_allowed':True,'other_destinations_rejected':True}
        instrument('isolated')
        apk=workspace/'app/build/outputs/apk/debug/app-debug.apk'
        boot=adb('shell','cat','/proc/sys/kernel/random/boot_id').stdout.strip()
        out={'schema':1,'time_utc':datetime.now(timezone.utc).isoformat(),'variant':variant,'avd':name,
             'source_commit':provenance['commit'],'apk_sha256':hashlib.sha256(apk.read_bytes()).hexdigest(),
             'boot_fingerprint':hashlib.sha256(boot).hexdigest(),'project':'demo-mpos-brain','policies':policies,
             'statuses':statuses,'observations':observations,'business_tests_allowed':True,
             'scope':'Dedicated guest app UID range, IPv4/IPv6, loopback via ADB; not a Windows-host firewall change'}
        public=ROOT/'evidence/firebase';public.mkdir(exist_ok=True)
        (public/(variant+'-network-gate.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
        (ROOT/'.local/flow-current-gate.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
        print(json.dumps({'business_tests_allowed':True,'variant':variant,'observations':observations},indent=2))
    finally:
        adb('shell','am','force-stop',package);adb('shell','rm','-f',remote,timeout=20)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--variant',choices=['flow-guarded','flow-rollback'],default='flow-guarded');p.add_argument('--serial',default='emulator-5586');p.add_argument('--verify-only',action='store_true');a=p.parse_args();run(a.variant,a.serial,a.verify_only)

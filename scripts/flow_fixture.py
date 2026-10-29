"""Import the preserved QA catalog into the dedicated isolated flow AVD once; never replace an existing DB."""
import hashlib
import json
from pathlib import Path
import sqlite3
import subprocess
ROOT=Path(__file__).resolve().parents[1]
ADB=Path('C:/Users/yejc2/AppData/Local/Android/Sdk/platform-tools/adb.exe')

def verify_gate(serial='emulator-5586',variant='flow-guarded'):
    def adb(*args):return subprocess.run([str(ADB),'-s',serial,*args],capture_output=True,timeout=30)
    if adb('emu','avd','name').stdout.decode('utf-8','replace').splitlines()[0]!='mPos_Brain_Flow_10_API35':raise ValueError('dedicated flow AVD required')
    gate=json.loads((ROOT/'.local/flow-current-gate.json').read_text())
    apk=ROOT/'.local/workspaces'/variant/'app/build/outputs/apk/debug/app-debug.apk'
    if not gate['business_tests_allowed'] or gate['apk_sha256']!=hashlib.sha256(apk.read_bytes()).hexdigest():raise ValueError('APK network gate missing or stale')
    if gate['boot_fingerprint']!=hashlib.sha256(adb('shell','cat','/proc/sys/kernel/random/boot_id').stdout.strip()).hexdigest():raise ValueError('AVD rebooted; reverify isolation')
    for family in ['iptables','ip6tables']:
        if adb('shell',family,'-w','-C','OUTPUT','-m','owner','--uid-owner','10000-199999','-j','MPOS_BRAIN_FLOW').returncode:raise ValueError('guest-app isolation hook absent')
        output=adb('shell',family,'-w','-S','OUTPUT').stdout.decode().splitlines()
        hooks=[line for line in output if line.startswith('-A OUTPUT ')]
        if not hooks or hooks[0].split()!=['-A','OUTPUT','-m','owner','--uid-owner','10000-199999','-j','MPOS_BRAIN_FLOW']:raise ValueError('guest-app reject policy is not first in OUTPUT')
        rules=[line.split() for line in adb('shell',family,'-w','-S','MPOS_BRAIN_FLOW').stdout.decode().splitlines() if line.startswith('-A ')]
        loopback='127.0.0.0/8' if family=='iptables' else '::1/128'
        if len(rules)!=2 or rules[0]!=['-A','MPOS_BRAIN_FLOW','-d',loopback,'-j','RETURN'] or rules[1][:4]!=['-A','MPOS_BRAIN_FLOW','-j','REJECT']:
            raise ValueError('guest-app isolation chain differs from verified loopback/reject policy')
    return adb

def main():
    adb=verify_gate();package='com.dtsgt.mpos.brainflow';adb('shell','am','force-stop',package)
    if adb('shell','test','-f','/sdcard/posdts.db').returncode==0:raise ValueError('flow database already exists; never replace it implicitly')
    schema=json.loads((ROOT/'catalog/runtime-qa-stage3-schema.json').read_text())
    candidates=[p for p in (ROOT/'.local/fixtures').glob('qa-after-stage3-*.db') if hashlib.sha256(p.read_bytes()).hexdigest()==schema['sqlite_sha256']]
    if len(candidates)!=1:raise ValueError('consistent third-stage snapshot not uniquely found')
    snapshot=candidates[0];db=sqlite3.connect(snapshot.resolve().as_uri()+'?mode=ro&immutable=1',uri=True)
    try:
        if db.execute('PRAGMA quick_check').fetchone()[0]!='ok':raise ValueError('snapshot inconsistent')
        for table in ['D_FACTURA','T_VENTA','T_PAGO']:
            if db.execute('SELECT COUNT(*) FROM '+table).fetchone()[0]:raise ValueError('source fixture has operational documents')
        if not db.execute('SELECT COUNT(*) FROM P_RES_MESA').fetchone()[0]:raise ValueError('restaurant catalogs not loaded')
    finally:db.close()
    if adb('push',str(snapshot),'/sdcard/posdts.db').returncode:raise RuntimeError('private fixture import failed')
    # Connection file contains only endpoint and timeout; remains private, and app egress is already blocked.
    source=ROOT/'.local/fixtures/qa-mposws.txt'
    copied=subprocess.run([str(ADB),'-s','emulator-5584','pull','/sdcard/mposws.txt',str(source)],capture_output=True,timeout=30)
    if copied.returncode==0:adb('push',str(source),'/sdcard/mposws.txt')
    metadata={'schema':1,'snapshot_sha256':schema['sqlite_sha256'],'catalog_tables':len(schema['tables']),
              'operational_documents_at_import':False,'network_gate_verified_before_import':True,'copied_to_dedicated_flow_avd':True}
    output=ROOT/'evidence/firebase/flow-fixture.json';output.write_text(json.dumps(metadata,indent=2),encoding='utf-8')
    print(json.dumps(metadata,indent=2))

if __name__=='__main__':main()

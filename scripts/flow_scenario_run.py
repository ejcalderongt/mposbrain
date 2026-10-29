"""Execute a versioned native-control recipe with isolated app state and structure-only public evidence."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
from flow_fixture import verify_gate
from lab_run import parse_status

ROOT=Path(__file__).resolve().parents[1]
ADB=Path('C:/Users/yejc2/AppData/Local/Android/Sdk/platform-tools/adb.exe')

def run(plan_path,variant,serial):
    adb=verify_gate(serial,variant);package='com.dtsgt.mpos.brainflow';plan=json.loads(plan_path.read_text(encoding='utf-8'))
    name=plan['id'];role=plan['role']
    if not re.fullmatch(r'[a-z][a-z0-9_]{2,60}',name) or role not in ('manager','waiter','cashier'):raise ValueError('invalid recipe identity')
    attempt=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S');private=ROOT/'.local/results/scenarios'/name/attempt;private.mkdir(parents=True,exist_ok=True)
    workspace=ROOT/'.local/workspaces'/variant
    if adb('install','-r','-g',str(workspace/'app/build/outputs/apk/androidTest/debug/app-debug-androidTest.apk')).returncode:raise RuntimeError('scenario test install failed')
    adb('shell','am','force-stop',package)
    adb('shell','run-as',package,'rm','-f','cache/brain-onboarding.jsonl','cache/brain-login-result.json','cache/brain-scenario.jsonl','cache/brain-scenario-private-dialogs.txt')
    selected=json.loads((ROOT/'.local/qa-selected-operators.json').read_text())[role];operator=private/'operator.json';operator.write_text(json.dumps(selected),encoding='utf-8')
    remotes=[]
    try:
        choices=json.loads((ROOT/'.local/flow-choices.json').read_text()) if '${' in plan_path.read_text(encoding='utf-8') else {}
        def resolve(value):
            if isinstance(value,dict):return {k:resolve(v) for k,v in value.items()}
            if isinstance(value,list):return [resolve(v) for v in value]
            if isinstance(value,str) and value.startswith('${') and value.endswith('}'):
                key=value[2:-1]
                if key not in {'group_label','mesa_id'}:raise ValueError('unknown private recipe choice')
                return str(choices[key])
            return value
        resolved=private/'resolved-plan.json';resolved.write_text(json.dumps(resolve(plan),indent=2),encoding='utf-8')
        for source,remote in [(operator,'/sdcard/Download/brain-operator.json'),(resolved,'/sdcard/Download/brain-flow-plan.json')]:
            if adb('push',str(source),remote).returncode:raise RuntimeError('private recipe fixture transfer failed')
            remotes.append(remote)
        result=subprocess.run([str(ADB),'-s',serial,'shell','am','instrument','-w','-r','-e','role',role,'-e','class','com.dtsgt.brainlabtests.FlowScenarioTest#executeNativeRecipe',package+'.test/androidx.test.runner.AndroidJUnitRunner'],capture_output=True,timeout=120+len(plan['steps'])*20)
        raw=(result.stdout+result.stderr).decode('utf-8','replace');(private/'instrumentation.txt').write_text(raw,encoding='utf-8')
        groups={}
        for key,file in [('events','brain-onboarding.jsonl'),('states','brain-scenario.jsonl')]:
            data=adb('exec-out','run-as',package,'cat','cache/'+file).stdout;(private/file).write_bytes(data)
            groups[key]=[json.loads(line) for line in data.decode('utf-8','replace').splitlines() if line.lstrip().startswith('{')]
        (private/'feedback-private.txt').write_bytes(adb('exec-out','run-as',package,'cat','cache/brain-scenario-private-dialogs.txt').stdout)
        allowed={'scenario','step','activity','runtimeRole','restaurantMode','globalOmitTip','sinPropina','propina','propinaperc','monto_propina','tot','diagnosticRenderedTip','diagnosticRenderedTotal','propina_vacia','rowCounts',
                 'elapsedMs','timeZone','peNoCierre','peSalon','pelCaja','needsWaiterPin','needsCashierPin','subLoginMode','paraLlevar','delivery','meseroPrecuenta','menus'}
        for row in groups['states']:
            if set(row)-allowed:raise ValueError('unexpected scenario state fields')
            if set(row.get('rowCounts',{}))-{'T_VENTA','T_PAGO','D_FACTURA','D_FACTURAPR','P_CAJACIERRE','T_ORDEN','T_ORDENCUENTA','T_RES_SESSION','P_RES_TURNO','D_USUARIO_ASISTENCIA'}:raise ValueError('unexpected database observation')
            for menu in row.get('menus',[]):
                if set(menu)-{'view','count','ids'} or any(not isinstance(i,int) for i in menu['ids']):raise ValueError('unexpected menu observation')
        for event in groups['events']:
            if set(event)-{'stage','received','activity','nodes'} or any(set(n)-{'id','type','visible','enabled','bounds'} for n in event['nodes']):raise ValueError('unsafe scenario UI observation')
        statuses=parse_status(raw)
        out={'schema':1,'scenario':name,'role':role,'attempt_id':attempt,'time_utc':datetime.now(timezone.utc).isoformat(),
             'source_commit':json.loads((workspace/'brain-lab-provenance.json').read_text())['commit'],
             'apk_sha256':hashlib.sha256((workspace/'app/build/outputs/apk/debug/app-debug.apk').read_bytes()).hexdigest(),
             'recipe_sha256':hashlib.sha256(plan_path.read_bytes()).hexdigest(),'network_gate_verified_before_run':True,
             'scope':plan['scope'],'statuses':statuses,**groups}
        public=ROOT/'evidence/flows';public.mkdir(exist_ok=True)
        (public/(name+'-attempt-'+attempt+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
        if statuses=={'executeNativeRecipe':'pass'}:(public/(name+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
        print(json.dumps({'scenario':name,'statuses':statuses,'activities':list(dict.fromkeys(r['activity'] for r in groups['states'])),'last_state':groups['states'][-1] if groups['states'] else None,'fingerprints':len(groups['events'])},indent=2))
        if statuses!={'executeNativeRecipe':'pass'}:raise RuntimeError('recipe stopped; inspect private feedback and current native state before the next action')
    finally:
        adb('shell','am','force-stop',package)
        for remote in remotes:adb('shell','rm','-f',remote)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--plan',type=Path,required=True);p.add_argument('--variant',choices=['flow-guarded','flow-rollback'],default='flow-guarded');p.add_argument('--serial',default='emulator-5586');a=p.parse_args();run(a.plan,a.variant,a.serial)

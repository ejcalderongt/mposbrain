"""Verify the dedicated loopback emulator with a synthetic REST round trip, then remove only that probe."""
from datetime import datetime,timezone
import json
from pathlib import Path
import urllib.request
import uuid
ROOT=Path(__file__).resolve().parents[1]

def main():
    hub=json.load(urllib.request.urlopen('http://127.0.0.1:19440/emulators',timeout=5))
    database=hub.get('database',{})
    if database.get('host')!='127.0.0.1' or database.get('port')!=19000:raise ValueError('unexpected local database endpoint')
    probe=uuid.uuid4().hex
    url='http://127.0.0.1:19000/BrainIsolationProbe/'+probe+'.json?ns=demo-mpos-brain-default-rtdb'
    expected={'synthetic':True,'marker':probe}
    try:
        request=urllib.request.Request(url,data=json.dumps(expected).encode(),method='PUT',headers={'Content-Type':'application/json'})
        with urllib.request.urlopen(request,timeout=5) as response:response.read()
        actual=json.load(urllib.request.urlopen(url,timeout=5))
        if actual!=expected:raise ValueError('local database round trip differs')
    finally:
        with urllib.request.urlopen(urllib.request.Request(url,method='DELETE'),timeout=5) as response:response.read()
    out={'schema':1,'time_utc':datetime.now(timezone.utc).isoformat(),'project':'demo-mpos-brain',
         'host':'127.0.0.1','port':19000,'synthetic_round_trip':True,'probe_removed':True,
         'scope':'Host-side loopback REST only; Android SDK routing and external-network isolation still require their own gate'}
    target=ROOT/'evidence/firebase';target.mkdir(exist_ok=True)
    (target/'host-probe.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))

if __name__=='__main__':main()

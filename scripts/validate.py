"""Validate public brain consistency, provenance and common accidental secret artifacts."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]

def validate(source=None):
    errors=[]
    summary=json.loads((ROOT/'catalog/scan-summary.json').read_text(encoding='utf-8'))
    inventory={}
    for name,count in summary['counts'].items():
        path=ROOT/'catalog'/(name+'.jsonl')
        rows=[json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
        if len(rows)!=count:errors.append(f'{name}: count mismatch')
        for row in rows:
            if row.get('line',1)<1:errors.append(f'{name}: invalid line')
            file=row.get('file','')
            if file and (file.startswith(('/', '\\')) or '..' in Path(file).parts):errors.append(f'{name}: non-relative provenance')
        if name=='inventory':inventory={r['file']:r for r in rows}
    if source:
        commit=subprocess.check_output(['git','-C',str(source),'rev-parse','HEAD']).decode().strip()
        if commit!=summary['source_commit']:errors.append('source commit drift: regenerate catalog')
        for relative,row in inventory.items():
            p=source/relative
            if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:
                errors.append('source content drift: '+relative)
    # Inspect the exact candidate publication set, including new files but excluding .gitignore paths.
    names=subprocess.check_output(['git','-C',str(ROOT),'ls-files','--cached','--others','--exclude-standard','-z']).decode().split('\0')
    prohibited={'.db','.sqlite','.sqlite3','.apk','.aab','.jks','.keystore','.hprof','.zip'}
    patterns=[r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',r'AIza[0-9A-Za-z_-]{30,}',
              r'AKIA[0-9A-Z]{16}',r'https?://[^\s/@]+:[^\s/@]+@',r'gh[pousr]_[A-Za-z0-9]{30,}']
    for name in set(names)-{''}:
        p=ROOT/name
        if p.suffix.lower() in prohibited or p.name in {'google-services.json','local.properties','qa-input.json'}:
            errors.append('prohibited artifact: '+name);continue
        raw=p.read_text(encoding='utf-8',errors='replace')
        if any(re.search(pattern,raw) for pattern in patterns):errors.append('possible secret; review privately: '+name)
    for required in ['README.md','AGENTS.md','HANDOFF.md','brain/INDEX.md','agent/skills/mpos-operational-agent/SKILL.md']:
        if not(ROOT/required).is_file():errors.append('missing '+required)
    return errors

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source',type=Path);args=p.parse_args()
    errors=validate(args.source)
    print(json.dumps({'passed':not errors,'errors':errors,'scope':'catalog consistency, optional source drift, common secret patterns; manual review still required'},indent=2))
    raise SystemExit(bool(errors))

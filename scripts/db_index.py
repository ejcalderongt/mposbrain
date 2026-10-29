"""Describe a consistent private SQLite snapshot without exporting row values, SQL defaults or file paths."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import re
import sqlite3

ROOT=Path(__file__).resolve().parents[1]

def describe(path):
    path=path.resolve()
    if not path.is_relative_to((ROOT/'.local').resolve()):raise ValueError('keep private SQLite snapshots under .local')
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    if path.read_bytes()[:16]!=b'SQLite format 3\x00':raise ValueError('not a SQLite database')
    db=sqlite3.connect(path.as_uri()+'?mode=ro&immutable=1',uri=True)
    try:
        tables=[]
        for (name,) in db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"):
            if not re.fullmatch(r'[A-Za-z_][A-Za-z_0-9]*',name):raise ValueError('unexpected table identifier; review privately')
            columns=[{'ordinal':r[0],'name':r[1],'type':r[2],'not_null':bool(r[3]),'has_default':r[4] is not None,'primary_key_position':r[5]}
                     for r in db.execute('PRAGMA table_info("'+name+'")')]
            count=db.execute('SELECT COUNT(*) FROM "'+name+'"').fetchone()[0]
            tables.append({'table':name,'row_count':count,'columns':columns})
        out={'schema':1,'time_utc':datetime.now(timezone.utc).isoformat(),'source':'private consistent QA snapshot',
             'sqlite_sha256':digest,'user_version':db.execute('PRAGMA user_version').fetchone()[0],
             'quick_check_ok':db.execute('PRAGMA quick_check').fetchone()[0]=='ok','tables':tables,
             'scope':'Schema and row counts only; input must be a consistent snapshot captured with WAL accounted for. No row/default/SQL text values exported.'}
    finally:db.close()
    if hashlib.sha256(path.read_bytes()).hexdigest()!=digest:raise ValueError('snapshot changed while reading')
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('database',type=Path);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    result=describe(args.database);args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({'tables':len(result['tables']),'quick_check_ok':result['quick_check_ok'],'user_version':result['user_version']}))

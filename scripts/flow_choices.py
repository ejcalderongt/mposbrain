"""Select an assigned group and ordinary table from the private received catalog, without changing data."""
import hashlib
import json
from pathlib import Path
import re
import sqlite3
ROOT=Path(__file__).resolve().parents[1]

def main():
    expected=json.loads((ROOT/'catalog/runtime-qa-stage3-schema.json').read_text())['sqlite_sha256']
    candidates=[p for p in (ROOT/'.local/fixtures').glob('qa-after-stage3-*.db') if hashlib.sha256(p.read_bytes()).hexdigest()==expected]
    if len(candidates)!=1:raise ValueError('third-stage baseline not unique')
    operator=json.loads((ROOT/'.local/qa-selected-operators.json').read_text())['waiter']
    profile=json.loads((ROOT/'.local/qa-profile.json').read_text())
    db=sqlite3.connect(candidates[0].resolve().as_uri()+'?mode=ro&immutable=1',uri=True)
    try:
        rows=db.execute('''SELECT g.CODIGO_GRUPO,g.NOMBRE,m.CODIGO_MESA,m.NOMBRE
            FROM P_RES_GRUPO g JOIN P_MESERO_GRUPO mg ON mg.CODIGO_GRUPO=g.CODIGO_GRUPO
            JOIN P_RES_MESA m ON m.CODIGO_GRUPO=g.CODIGO_GRUPO
            WHERE mg.CODIGO_MESERO=? AND g.CODIGO_SUCURSAL=? AND m.CODIGO_SUCURSAL=?
            ORDER BY g.CODIGO_GRUPO,m.CODIGO_MESA''',(operator['CODIGO_VENDEDOR'],profile['store'],profile['store'])).fetchall()
        normal=[r for r in rows if str(r[3]).strip().isdigit() and not re.search('llevar|domicilio|delivery|express',str(r[1]),re.I)]
        if not normal:raise ValueError('ordinary assigned test table not found; inspect/ask instead of guessing')
        group,label,table,table_label=normal[0]
        count=db.execute('SELECT COUNT(*) FROM P_RES_MESA WHERE CODIGO_GRUPO=?',(group,)).fetchone()[0]
    finally:db.close()
    (ROOT/'.local/flow-choices.json').write_text(json.dumps({'group_label':label,'mesa_id':str(table),'expected_group_tables':count,'source_snapshot_sha256':expected},indent=2),encoding='utf-8')
    print(json.dumps({'assigned_group_found':True,'ordinary_table_found':True,'tables_in_group':count,'data_modified':False}))

if __name__=='__main__':main()

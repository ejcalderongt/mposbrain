import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('config_index',Path(__file__).resolve().parents[1]/'scripts/config_index.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class ConfigIndexTests(unittest.TestCase):
    def test_nested_lookups_are_not_attributed_to_parent_and_string_defaults_are_not_exported(self):
        raw=b'''class Example { void configure() {
            try { sql="SELECT VALOR FROM P_PARAMEXT WHERE ID=118";
                gl.peRest=val.equalsIgnoreCase("S");
                try { sql="SELECT VALOR FROM P_PARAMEXT WHERE ID=120"; gl.pePropinaPerc=amount; }
                catch(Exception e) { gl.pePropinaPerc=0; }
            } catch(Exception e) { gl.peRest=false; gl.endpoint="sample-private-input"; }
        }}'''
        rows=module.extract(raw,'fixture.java')
        self.assertEqual(len(rows),2)
        outer=next(r for r in rows if r['parameter_ids']==[118]);inner=next(r for r in rows if r['parameter_ids']==[120])
        self.assertNotIn('pePropinaPerc',[w['global'] for w in outer['global_writes']])
        self.assertEqual(next(w for w in outer['global_writes'] if w['global']=='peRest' and w['phase']=='catch')['literal'],False)
        self.assertEqual(next(w for w in inner['global_writes'] if w['phase']=='catch')['literal'],0)
        self.assertNotIn('sample-private-input',str(rows))

if __name__=='__main__':unittest.main()

import importlib.util
import json
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('trace_analyze',Path(__file__).resolve().parents[1]/'scripts/trace_analyze.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class TraceTests(unittest.TestCase):
    def test_interleaved_sessions_do_not_invent_routes_and_values_are_not_exported(self):
        records=[{'session':'private-session-a','seq':1,'event':'activity_resumed','data':{'activity':'MainActivity','key':'private-input'}},
                 {'session':'private-session-b','seq':1,'event':'activity_resumed','data':{'activity':'Pago'}},
                 {'session':'private-session-a','seq':3,'event':'activity_resumed','data':{'activity':'WSRec'}},
                 {'session':'private-session-a','seq':4,'event':'tip_guard_inherited_zero_match','data':{'stateDiffersFromRendered':True}}]
        result=module.analyze([json.dumps(r) for r in records]+['truncated record'])
        self.assertEqual(result['observed_resume_transitions'],[{'from':'MainActivity','to':'WSRec','count':1}])
        self.assertEqual(result['quality']['invalid_lines'],1)
        self.assertEqual(result['quality']['missing_sequence_slots'],1)
        self.assertEqual(result['anomaly_observations']['model_render_difference'],1)
        self.assertNotIn('private-input',json.dumps(result));self.assertNotIn('private-session',json.dumps(result))

if __name__=='__main__':unittest.main()

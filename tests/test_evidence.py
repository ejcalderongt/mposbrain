import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('lab_run',ROOT/'scripts/lab_run.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class EvidenceTests(unittest.TestCase):
    def test_instrumentation_failure_is_distinct_from_infrastructure_error(self):
        raw='''INSTRUMENTATION_STATUS: test=tipContract
INSTRUMENTATION_STATUS_CODE: 1
INSTRUMENTATION_STATUS: test=tipContract
INSTRUMENTATION_STATUS_CODE: -2
INSTRUMENTATION_STATUS: test=runnerError
INSTRUMENTATION_STATUS_CODE: -1
INSTRUMENTATION_STATUS: test=control
INSTRUMENTATION_STATUS_CODE: 0
'''
        self.assertEqual(module.parse_status(raw),{'tipContract':'fail','runnerError':'error','control':'pass'})

    def test_incomplete_test_cannot_be_counted_as_pass(self):
        self.assertEqual(module.parse_status('INSTRUMENTATION_STATUS: test=incomplete\nINSTRUMENTATION_STATUS_CODE: 1'),{})

if __name__=='__main__':unittest.main()

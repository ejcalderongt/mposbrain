"""Share the structure-only UI observation harness with real-control flow tests."""
import argparse
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def prepare(variant):
    workspace=ROOT/'.local/workspaces'/variant
    prefix=(ROOT/'experiments/onboarding/QaBootstrapTest.java.template').read_text(encoding='utf-8').split('    @Test public void emptyDatabaseOpensCommunicationAndReceivesQa()',1)[0]
    prefix=prefix.replace('public class QaBootstrapTest','public class FlowLoginTest').replace('private ','protected ')
    target=workspace/'app/src/brainFlowTest/java/com/dtsgt/brainlabtests/FlowLoginTest.java'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(prefix+(ROOT/'experiments/firebase/FlowLoginTest.java.body').read_text(encoding='utf-8'),encoding='utf-8')
    scenario=workspace/'app/src/brainFlowTest/java/com/dtsgt/brainlabtests/FlowScenarioTest.java'
    scenario.write_text((ROOT/'experiments/firebase/FlowScenarioTest.java.template').read_text(encoding='utf-8'),encoding='utf-8')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--variant',choices=['flow-guarded','flow-rollback'],default='flow-guarded');prepare(p.parse_args().variant)

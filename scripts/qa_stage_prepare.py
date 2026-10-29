"""Build the staged receive test from the shared structure-only observation harness."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def prepare():
    prefix=(ROOT/'experiments/onboarding/QaBootstrapTest.java.template').read_text(encoding='utf-8').split('    @Test public void emptyDatabaseOpensCommunicationAndReceivesQa()',1)[0]
    prefix=prefix.replace('public class QaBootstrapTest','public class QaStagedReceiveTest')
    target=ROOT/'.local/workspaces/qa/app/src/brainTest/java/com/dtsgt/brainlabtests/QaStagedReceiveTest.java'
    target.write_text(prefix+(ROOT/'experiments/onboarding/QaStagedReceiveTest.java.body').read_text(encoding='utf-8'),encoding='utf-8')

if __name__=='__main__':prepare()

"""Check the expected A/B outcome; infrastructure errors never count as successful reproduction."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REGRESSIONS={'tipNotLostAfterWithoutThenWith','explicitWithTipRecoversInheritedPercentage',
             'variableTipAppearsInFooter','documentExceptionCannotReportSuccess','failedBuildCannotDispatchOlderReceipt'}
CONTROLS={'fixedTipFooterStillWorks','explicitChoiceKeepsExclusions'}

def check(guarded,rollback):
    errors=[]
    expected=REGRESSIONS|CONTROLS
    for name,data in [('guarded',guarded),('rollback',rollback)]:
        if set(data['statuses'])!=expected:errors.append(name+': missing or unexpected tests')
        if len(data['observations'])!=7:errors.append(name+': observation count mismatch')
        if data['network_permission'] or not data['dedicated_avd']:errors.append(name+': isolation failed')
        for test,status in data['statuses'].items():
            wanted='fail' if name=='rollback' and test in REGRESSIONS else 'pass'
            if status!=wanted:errors.append(name+': unexpected '+test+' status '+status)
    return errors

def main():
    root=ROOT/'evidence/experiments'
    g=json.loads((root/'guarded.json').read_text());r=json.loads((root/'rollback.json').read_text())
    errors=check(g,r)
    if errors:raise RuntimeError('; '.join(errors))
    rows={v['case']:v for v in r['observations']}
    result={'expected_contrast_confirmed':True,'guarded_pass':7,'rollback_regressions':5,'controls_pass_both':2,
            'rollback_tip_after_without_then_with':rows['without_then_with']['printedWithTipAfterward'],
            'rollback_percentage_after_explicit_with':rows['explicit_with_tip']['percentageAtPrint'],
            'rollback_old_tip_artifact_dispatched':rows['stale_receipt_dispatch']['oldTipArtifactDispatched'],
            'scope':'Android component/extracted-source contracts with synthetic fixtures; not full UI, physical printer or historical customer root cause'}
    (root/'comparison.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()

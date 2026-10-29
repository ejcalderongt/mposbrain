"""Summarize sanitized DiagnosticLog JSONL without publishing account/session identifiers or input values."""
import argparse
from collections import Counter,defaultdict
import json
from pathlib import Path

def analyze(lines):
    events=Counter();matches=Counter();anomalies=Counter();routes=Counter();last_activity={};last_seq={}
    invalid=0;out_of_order=0;missing_sequence_slots=0;max_dropped=0
    for line in lines:
        try:row=json.loads(line)
        except (ValueError,TypeError):invalid+=1;continue
        event=row.get('event');session=row.get('session');seq=row.get('seq');data=row.get('data',{})
        if not isinstance(event,str) or not isinstance(data,dict):invalid+=1;continue
        events[event]+=1
        if event.endswith('_match'):matches[event]+=1
        if data.get('rowMissing') is True:anomalies['positive_tip_row_missing']+=1
        if data.get('stateDiffersFromRendered') is True:anomalies['model_render_difference']+=1
        if isinstance(seq,int) and session:
            if session in last_seq:
                delta=seq-last_seq[session]
                if delta<=0:out_of_order+=1
                elif delta>1:missing_sequence_slots+=delta-1
            last_seq[session]=seq
        dropped=row.get('droppedSoFar',0)
        if isinstance(dropped,int):max_dropped=max(max_dropped,dropped)
        if event=='activity_resumed':
            activity=data.get('activity')
            # Only Java-style activity identifiers are allowed in an exported path.
            if isinstance(activity,str) and activity.isidentifier():
                previous=last_activity.get(session)
                if previous:routes[(previous,activity)]+=1
                last_activity[session]=activity
    return {'schema':1,'events':dict(events),'guard_matches':dict(matches),'anomaly_observations':dict(anomalies),
            'observed_resume_transitions':[{'from':a,'to':b,'count':n} for (a,b),n in sorted(routes.items())],
            'quality':{'invalid_lines':invalid,'out_of_order_or_duplicate_records':out_of_order,
                       'missing_sequence_slots':missing_sequence_slots,'max_reported_dropped':max_dropped},
            'interpretation':'Observed transitions include returns, not necessarily direct Intent edges. Matches/anomalies are candidates, not a causal verdict. Missing slots can result from rotation or partial extraction.'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    result=analyze(args.input.read_text(encoding='utf-8').splitlines())
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({'records':sum(result['events'].values()),'matches':sum(result['guard_matches'].values()),'quality':result['quality']}))

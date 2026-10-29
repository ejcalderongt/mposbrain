"""Query exported catalogs without loading private application sources."""
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('catalog',help='catalog stem, e.g. navigation or global_state')
    p.add_argument('term');p.add_argument('--limit',type=int,default=20)
    p.add_argument('--where',action='append',default=[],help='exact top-level field=value filter; repeatable')
    args=p.parse_args()
    path=(ROOT/'catalog'/(args.catalog+'.jsonl')).resolve()
    if path.parent!=(ROOT/'catalog').resolve(): raise ValueError('invalid catalog')
    count=0
    filters=[item.split('=',1) for item in args.where]
    if any(len(item)!=2 for item in filters):raise ValueError('where requires field=value')
    for line in path.open(encoding='utf-8'):
        if args.term.casefold() in line.casefold():
            row=json.loads(line)
            if any(str(row.get(key))!=value for key,value in filters):continue
            print(json.dumps(row,ensure_ascii=False));count+=1
            if count>=args.limit:break

if __name__=='__main__':main()

"""Query exported catalogs without loading private application sources."""
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('catalog',help='catalog stem, e.g. navigation or global_state')
    p.add_argument('term');p.add_argument('--limit',type=int,default=20)
    args=p.parse_args()
    path=(ROOT/'catalog'/(args.catalog+'.jsonl')).resolve()
    if path.parent!=(ROOT/'catalog').resolve(): raise ValueError('invalid catalog')
    count=0
    for line in path.open(encoding='utf-8'):
        if args.term.casefold() in line.casefold():
            print(json.dumps(json.loads(line),ensure_ascii=False));count+=1
            if count>=args.limit:break

if __name__=='__main__':main()

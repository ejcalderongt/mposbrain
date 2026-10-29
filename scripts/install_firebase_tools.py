"""Install a pinned official standalone Firebase CLI under the private lab folder."""
import hashlib
from pathlib import Path
import urllib.request
ROOT=Path(__file__).resolve().parents[1]
VERSION='15.34.2'
URL='https://github.com/firebase/firebase-tools/releases/download/v'+VERSION+'/firebase-tools-win.exe'
SHA='ce94c49acfb6349bddb6a79f3730e187d25ccc59daac42906d1c2c63243beebc'

def main():
    target=ROOT/'.local/tools/firebase-tools-win.exe';target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():
        if hashlib.sha256(target.read_bytes()).hexdigest()!=SHA:raise ValueError('existing Firebase tool differs; preserve and inspect')
    else:
        temporary=target.with_suffix('.download')
        urllib.request.urlretrieve(URL,temporary)
        if hashlib.sha256(temporary.read_bytes()).hexdigest()!=SHA:raise ValueError('Firebase release digest mismatch')
        temporary.rename(target)
    print('Verified Firebase CLI '+VERSION+' installed privately')

if __name__=='__main__':main()

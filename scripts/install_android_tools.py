"""Install official Android command-line tools with verified archive hash; no existing installation overwrite."""
import hashlib
import os
from pathlib import Path
import urllib.request
import zipfile

ROOT=Path(__file__).resolve().parents[1]
URL='https://dl.google.com/android/repository/commandlinetools-win-15859902_latest.zip'
SHA='90ae805d20434428bffcb699c290860f19bb5f66a67e6b330067e3de801fb04a'

def main():
    sdk=Path(os.environ['LOCALAPPDATA'])/'Android/Sdk'
    target=sdk/'cmdline-tools/brain-23'
    if target.exists():
        if (target/'bin/sdkmanager.bat').is_file():print('Android command-line tools already installed');return
        raise ValueError('incomplete existing installation; inspect before replacing')
    archive=ROOT/'.local/android-tools.zip';archive.parent.mkdir(exist_ok=True)
    urllib.request.urlretrieve(URL,archive)
    if hashlib.sha256(archive.read_bytes()).hexdigest()!=SHA:raise ValueError('official archive checksum mismatch')
    with zipfile.ZipFile(archive) as z:
        for member in z.infolist():
            parts=Path(member.filename).parts
            if not parts or parts[0]!='cmdline-tools' or '..' in parts:raise ValueError('unexpected archive layout')
            relative=Path(*parts[1:])
            if not str(relative) or member.is_dir():continue
            destination=target/relative;destination.parent.mkdir(parents=True,exist_ok=True)
            destination.write_bytes(z.read(member))
    print('Verified official Android command-line tools installed in '+str(target))

if __name__=='__main__':main()

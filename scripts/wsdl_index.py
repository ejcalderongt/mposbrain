"""Export interface names and parameter types from private WSDL, never defaults or endpoint addresses."""
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
NS={'w':'http://schemas.xmlsoap.org/wsdl/','x':'http://www.w3.org/2001/XMLSchema'}

def main():
    private=ROOT/'.local/qa-wsdl.xml';raw=private.read_bytes();root=ET.fromstring(raw)
    operations=sorted({n.get('name') for n in root.findall('w:portType/w:operation',NS)})
    params={}
    for element in root.findall('w:types/x:schema/x:element',NS):
        name=element.get('name')
        if name not in operations:continue
        params[name]=[{'name':n.get('name'),'type':n.get('type'),'min_occurs':n.get('minOccurs','1')}
                      for n in element.findall('x:complexType/x:sequence/x:element',NS)]
    out={'source':'user-authorized AWS QA WSDL','sha256':hashlib.sha256(raw).hexdigest(),
         'operations':operations,'input_parameters':params,
         'scope':'Published interface only; operation presence does not prove authorization or actual use by a configured client'}
    (ROOT/'catalog/wsdl-operations.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({'operations':len(operations),'parameter_lists':len(params)}))

if __name__=='__main__':main()

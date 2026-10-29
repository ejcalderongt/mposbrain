"""Run bounded Java source probes from the fetched original branch; never check out or modify mPos."""
import hashlib
import json
from pathlib import Path
import subprocess
from lab_prepare import PARSER, walk

ROOT=Path(__file__).resolve().parents[1]
SOURCE=Path('C:/Users/yejc2/source/repos/mPos2025')
JDK=Path('C:/Program Files/Microsoft/jdk-17.0.20.101-hotspot/bin')

def git(*args):
    return subprocess.check_output(['git','-C',str(SOURCE),*args])

def methods(commit,path):
    raw=git('show',commit+':'+path).removeprefix(b'\xef\xbb\xbf')
    tree=PARSER.parse(raw)
    if tree.root_node.has_error:raise ValueError('Java parse error')
    return [(raw[n.child_by_field_name('name').start_byte:n.child_by_field_name('name').end_byte].decode(),raw[n.start_byte:n.end_byte].decode(),n.start_point.row+1) for n in walk(tree.root_node) if n.type=='method_declaration']

def main():
    commit=git('rev-parse','origin/dev626b').decode().strip()
    base='b12b47665a28bafb57f4bb85de989b31b0b2613b'
    private=ROOT/'.local/reviews'/commit;private.mkdir(parents=True,exist_ok=True)
    paths={'calc':'app/src/main/java/com/dtsgt/mpos/FacturaRes.java','footer':'app/src/main/java/com/dtsgt/classes/clsDocCuenta.java','document':'app/src/main/java/com/dtsgt/classes/clsDocument.java'}
    current={k:methods(commit,p) for k,p in paths.items()}
    previous={k:methods(base,p) for k,p in paths.items()}
    def get(which,name,rows=current,predicate=lambda s:True):
        found=[(code,line) for n,code,line in rows[which] if n==name and predicate(code)]
        if len(found)!=1:raise ValueError('ambiguous source method '+name)
        return found[0]
    total=get('calc','totalOrder')[0];cortesia=get('calc','totalOrderCortesia')[0]
    footer=get('footer','footerBaseGUA')[0]
    document=get('document','buildPrint',predicate=lambda s:'String pmesa' in s)[0]
    init=get('calc','onCreate')[0]
    anchor='perc_propina = gl.pePropinaPerc;'
    if init.count(anchor)!=1 or 'gl.propina_vacia' in init:raise ValueError('initializer changed; reassess extraction')
    java='''public class TipBranchProbe {
 static class Globals {double pePropinaPerc=10,propina_valor; boolean pePropinaFija=true,peRedondPropina,propina_vacia,parallevar,peLlevarSinPropina,sin_propina;}
 static class Mu {double round2(double v){return Math.round(v*100)/100.0;} double roundtoint(double v){return Math.round(v);} void msgbox(String s){} }
 static class Calc {
 Globals gl=new Globals(); Mu mu=new Mu(); boolean cleandprod,acum,EsNivelPrecioDelivery;
 double stot0=135,stot,propina,propinaperc,propinaext,perc_propina,descgmon,descaddmonto,dfinmon,descpmon,dmax,descmon,descimp;
 void addlog(String a,String b,String c){} void msgbox(String s){} void fillTotals(){}
 void initialize(){__INIT__}
 __TOTAL__
 __CORTESIA__
 }
 static class Rep {boolean tip,total,saveOk=true; void addtotsppr(String s,double v){if(s.startsWith("Propina:"))tip=true;if(s.startsWith("TOTAL"))total=true;} void addtotsp(String s,double v){} void add(String s){} void line(){} void clear(){} boolean save(){return saveOk;}}
 static class FooterBase {protected boolean buildFooter(){return true;}}
 static class Footer extends FooterBase {
 double ptotal=148.5,pdesc,propvalor=13.5,pprop;boolean propfija,precuenta1015;String vendedor="synthetic";Rep rep=new Rep();
 int roundtoint(double v){return (int)Math.round(v);}
 __FOOTER__
 }
 static class Document {Rep rep=new Rep();String mesa,cuenta;double ptotal,pdesc,pprop,propvalor,propperc;boolean propfija,throwHeader;
 boolean buildHeader(){if(throwHeader)throw new RuntimeException("synthetic");return true;} boolean buildDetail(){return true;} boolean buildFooter(){return true;}
 void setAddlog(String a,String b,String c){}
 __DOCUMENT__
 }
 public static void main(String[] args){
 Calc c=new Calc();c.gl.propina_vacia=true;c.initialize();c.totalOrder();System.out.println("inherited_flag_tip="+c.propina);
 c.gl.sin_propina=true;c.totalOrder();System.out.println("excluded_tip="+c.propina);
 c.gl.sin_propina=false;c.totalOrderCortesia();System.out.println("explicit_removed_tip="+c.propina);c.propinaext=0;c.totalOrder();System.out.println("extra_zero_after_remove_tip="+c.propina);
 Footer f=new Footer();f.footerBaseGUA();System.out.println("variable_footer_tip_present="+f.rep.tip);System.out.println("variable_footer_total_present="+f.rep.total);
 Document d=new Document();d.throwHeader=true;System.out.println("exception_reports_success="+d.buildPrint("synthetic","1",148.5,0,10,true,13.5));
 d.throwHeader=false;d.rep.saveOk=false;System.out.println("save_failure_reports_success="+d.buildPrint("synthetic","1",148.5,0,10,true,13.5));
 }
}'''
    for a,b in {'__INIT__':anchor,'__TOTAL__':total,'__CORTESIA__':cortesia,'__FOOTER__':footer,'__DOCUMENT__':document}.items():java=java.replace(a,b)
    (private/'TipBranchProbe.java').write_text(java,encoding='utf-8')
    subprocess.run([str(JDK/'javac.exe'),'-encoding','UTF-8',str(private/'TipBranchProbe.java')],check=True,capture_output=True)
    output=subprocess.check_output([str(JDK/'java.exe'),'-cp',str(private),'TipBranchProbe']).decode()
    values={}
    for line in output.splitlines():
        k,v=line.split('=');values[k]=v=='true' if v in ('true','false') else float(v)
    checks={'inherited_flag_tip':13.5,'excluded_tip':13.5,'explicit_removed_tip':0.0,'extra_zero_after_remove_tip':13.5,'variable_footer_tip_present':False,'variable_footer_total_present':False,'exception_reports_success':True,'save_failure_reports_success':False}
    if values!=checks:raise ValueError('probe expectation changed; inspect private output')
    origins=[]
    for key,name,pred in [('calc','totalOrder',lambda s:True),('calc','totalOrderCortesia',lambda s:True),('footer','footerBaseGUA',lambda s:True),('document','buildPrint',lambda s:'String pmesa' in s)]:
        code,line=get(key,name,predicate=pred)
        old=get(key,name,rows=previous,predicate=pred)[0]
        origins.append({'file':paths[key],'method':name,'line':line,'sha256':hashlib.sha256(code.encode()).hexdigest(),'unchanged_from_original_baseline':code==old})
    primary=get('calc','impresionCuenta')[0]
    report={'schema':1,'commit':commit,'baseline':base,'scope':'JDK17 execution of extracted real methods with synthetic fields, no Android UI/DB/physical printer; fillTotals stubbed','observations':values,'origins':origins,'primary_print_still_ignores_build_result':'\n\t\t\tfdoc.buildPrint(' in primary,'primary_without_tip_mutation_removed':'tot = tot - propina' not in primary,'without_tip_button_removed':b'prnCuentaSin' not in git('show',commit+':app/src/main/res/layout/activity_factura_res_precue.xml')}
    target=ROOT/'evidence/reviews';target.mkdir(exist_ok=True)
    (target/('jaros-'+commit[:8]+'.json')).write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()

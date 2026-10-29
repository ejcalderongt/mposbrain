"""Create a private restaurant-flow clone with a demo Firebase project; network gate still required."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]
REFS={'flow-guarded':'bd94c90c','flow-rollback':'c21e92ec'}

def prepare(source,variant):
    workspace=ROOT/'.local/workspaces'/variant
    if workspace.exists():raise ValueError('existing flow workspace must be inspected/reused, never silently replaced')
    subprocess.run(['git','clone','--quiet','--no-hardlinks',str(source),str(workspace)],check=True)
    subprocess.run(['git','-C',str(workspace),'checkout','--quiet','--detach',REFS[variant]],check=True)
    package='com.dtsgt.mpos.brainflow'
    appgradle=workspace/'app/build.gradle'
    appgradle.write_text(appgradle.read_text(encoding='utf-8')+'''
// Private flow laboratory only. External network must be blocked by the runner before business tests.
android {
 defaultConfig { applicationId "com.dtsgt.mpos.brainflow"; testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner" }
 sourceSets { androidTest.java.srcDirs = ['src/brainFlowTest/java'] }
}
dependencies {
 androidTestImplementation 'androidx.test:runner:1.7.0'
 androidTestImplementation 'androidx.test.ext:junit:1.3.0'
}
''',encoding='utf-8')
    fake={'project_info':{'project_number':'1234567890','project_id':'demo-mpos-brain',
          'firebase_url':'https://demo-mpos-brain-default-rtdb.firebaseio.com','storage_bucket':'demo-mpos-brain.appspot.com'},
          'client':[{'client_info':{'mobilesdk_app_id':'1:1234567890:android:00112233445566778899aabbccddeeff','android_client_info':{'package_name':package}},
          'oauth_client':[],'api_key':[{'current_key':'AIza'+'A'*35}],'services':{'appinvite_service':{'other_platform_oauth_client':[]}}}],
          'configuration_version':'1'}
    (workspace/'app/google-services.json').write_text(json.dumps(fake,indent=2),encoding='utf-8')
    manifest=workspace/'app/src/main/AndroidManifest.xml';text=manifest.read_text(encoding='utf-8')
    text=text.replace('android:usesCleartextTraffic="true"','android:usesCleartextTraffic="false" android:networkSecurityConfig="@xml/brain_network_security"')
    for key in ['firebase_analytics_collection_enabled','firebase_crashlytics_collection_enabled','firebase_performance_collection_enabled','firebase_messaging_auto_init_enabled','firebase_data_collection_default_enabled']:
        text=text.replace('</application>',f'<meta-data android:name="{key}" android:value="false" />\n</application>')
    text=text.replace('</application>','<meta-data android:name="firebase_performance_collection_deactivated" android:value="true" />\n</application>')
    manifest.write_text(text,encoding='utf-8')
    network=workspace/'app/src/main/res/xml/brain_network_security.xml';network.parent.mkdir(exist_ok=True)
    network.write_text('''<?xml version="1.0" encoding="utf-8"?>
<network-security-config><base-config cleartextTrafficPermitted="false" />
<domain-config cleartextTrafficPermitted="true"><domain>127.0.0.1</domain><domain>localhost</domain></domain-config>
</network-security-config>''',encoding='utf-8')
    globals_path=workspace/'app/src/main/java/com/dtsgt/base/appGlobals.java';text=globals_path.read_text(encoding='utf-8')
    if text.count('super.onCreate();')!=1:raise ValueError('Application observer anchor drift')
    text=text.replace('super.onCreate();','super.onCreate();\n com.dtsgt.brainlab.BrainLabEnvironment.configure(this);',1)
    globals_path.write_text(text,encoding='utf-8')
    for template,relative in [('BrainLabEnvironment.java.template','app/src/main/java/com/dtsgt/brainlab/BrainLabEnvironment.java'),
                              ('NetworkGateTest.java.template','app/src/brainFlowTest/java/com/dtsgt/brainlabtests/NetworkGateTest.java')]:
        target=workspace/relative;target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text((ROOT/'experiments/firebase'/template).read_text(encoding='utf-8'),encoding='utf-8')
    (workspace/'local.properties').write_text('sdk.dir=C:/Users/yejc2/AppData/Local/Android/Sdk\n',encoding='utf-8')
    (workspace/'.gradle').mkdir(exist_ok=True)
    (workspace/'.gradle/config.properties').write_text('java.home=C:/Program Files/Microsoft/jdk-17.0.20.101-hotspot\n',encoding='utf-8')
    provenance={'variant':variant,'commit':subprocess.check_output(['git','-C',str(workspace),'rev-parse','HEAD']).decode().strip(),
                'application_id':package,'network_permission':True,'network_isolation':'not yet established; requires UID firewall + Android gate before business writes',
                'firebase_project':'demo-mpos-brain','firebase_database':'127.0.0.1:19000 via ADB reverse',
                'test_seams':['demo Firebase options and emulator routing before Activity creation','collection and messaging auto-init disabled','loopback-only cleartext'],
                'source_repo_modified':False}
    (workspace/'brain-lab-provenance.json').write_text(json.dumps(provenance,indent=2),encoding='utf-8')
    print(json.dumps({'variant':variant,'application_id':package,'source_commit':provenance['commit'],'business_tests_allowed':False}))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source',type=Path,required=True);p.add_argument('--variant',choices=REFS,required=True);a=p.parse_args();prepare(a.source,a.variant)

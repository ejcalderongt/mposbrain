$ErrorActionPreference = 'Stop'
$brainRoot = Split-Path -Parent $PSScriptRoot
$avdRoot = Join-Path $env:USERPROFILE '.android/avd'
$flowName = 'mPos_Brain_Flow_10_API35'
$flowDirectory = Join-Path $avdRoot ($flowName + '.avd')
$sourceConfig = Join-Path $avdRoot 'mPos_Brain_QA_10_API35.avd/config.ini'
if (Test-Path -LiteralPath $flowDirectory) { throw 'Flow AVD already exists; inspect and reuse it instead of replacing data' }
$sdkDirectory = Join-Path $env:LOCALAPPDATA 'Android/Sdk'
if (-not (Test-Path -LiteralPath (Join-Path $sdkDirectory 'system-images/android-35/google_apis/x86_64/source.properties'))) { throw 'API 35 Google APIs image required' }
$config = Get-Content -Raw -LiteralPath $sourceConfig
$config = $config.Replace('mPos_Brain_QA_10_API35', $flowName).Replace('mPos Brain QA 10 pulgadas', 'mPos Brain Flow 10 pulgadas').Replace('hw.ramSize=2048','hw.ramSize=4096')
New-Item -ItemType Directory -Path $flowDirectory | Out-Null
Set-Content -LiteralPath (Join-Path $flowDirectory 'config.ini') -Value $config
$ini = "avd.ini.encoding=UTF-8`npath=$flowDirectory`npath.rel=avd\$flowName.avd`ntarget=android-35"
Set-Content -LiteralPath (Join-Path $avdRoot ($flowName + '.ini')) -Value $ini
$privateDirectory = Join-Path $brainRoot '.local'
Start-Process -FilePath (Join-Path $sdkDirectory 'emulator/emulator.exe') -ArgumentList "-avd $flowName -port 5586 -no-window -no-audio -no-snapshot-load -no-snapshot-save -dns-server 8.8.8.8,1.1.1.1" -WindowStyle Hidden -RedirectStandardOutput (Join-Path $privateDirectory 'flow-emulator-out.txt') -RedirectStandardError (Join-Path $privateDirectory 'flow-emulator-err.txt')
Write-Output 'Created dedicated flow AVD on emulator-5586; no application installed or business writes authorized until network gate passes'

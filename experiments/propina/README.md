# Contratos A/B de propina

Estos contratos corren en Android con importes sintéticos. No son una simulación completa del restaurante ni de la impresora. Se extraen bloques desde AST del commit bajo prueba y se ejercita el generador de documentos real con un encabezado DB sustituido.

Preparación: scripts/lab_prepare.py --source <checkout> --variant guarded, rollback o qa. Compilación: scripts/lab_build.py --variant <variante>. Ejecución offline: scripts/lab_run.py --variant guarded --serial emulator-5580; repetir con rollback.

Se espera que guarded supere siete contratos; rollback falle cinco y supere dos controles. Los cinco fallos esperados son evidencia de mecanismos reproducibles. Errores del runner, falta de observaciones o excepciones de infraestructura no cuentan como reproducción.

Las observaciones y procedencia se exportan a evidence/experiments. .local conserva clones, compilación y salidas crudas privadas. El script exige el AVD dedicado y ausencia de INTERNET. Los APK nunca se versionan.

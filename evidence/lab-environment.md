# Entorno de laboratorio

AVD offline dedicado: mPos_Brain_Lab_10, 10 pulgadas, 1280x800, Android API 37. Paquete de contratos com.dtsgt.mpos.brainlab, runner AndroidJUnitRunner. Se compilan snapshots de commits en clones ignorados; no se modifica el checkout habitual.

Los APK offline no tienen permiso INTERNET, comprobado por aapt antes de instalar. Al primer intento, Firebase Installations intentó registrarse pese a tener desactivada la recolección y provocó una SecurityException por la ausencia del permiso. Ese intento fue fallo de infraestructura y no se contó como resultado de los contratos.

Corrección exclusiva del laboratorio: retirar FirebaseInitProvider del manifest de todas las variantes. No altera los cuatro mecanismos de propina. El segundo intento de guarded completó siete contratos con siete observaciones. Los detalles y hashes están en experiments/guarded.json.

Las pruebas sustituyen el encabezado dependiente de base y la impresora física, y extraen bloques de fuente para aspectos de Activity. El porcentaje recuperado se comprueba antes de cálculo completo. No demuestran un recorrido de UI completo, una impresión física ni la causa histórica del incidente del cliente.

El arranque limpio del primer AVD QA con imagen API 37.2 presentó fallos de componentes del sistema antes de ejecutar mPos. Se instaló adicionalmente system-images;android-35;google_apis;x86_64 para un AVD QA nuevo, mPos_Brain_QA_10_API35, puerto 5584. Esto no cambia la plataforma del contraste A/B, que fue API 37 para ambas variantes.

Para instalar la imagen se agregaron las herramientas oficiales de línea de comandos, verificando SHA-256 del ZIP contra la [página oficial de Android](https://developer.android.com/studio). La instalación vive bajo SDK/cmdline-tools/brain-23. El script conserva URL y hash verificados; no reemplaza una instalación existente.

Detalle de diagnóstico del host: con -no-window el ejecutable es qemu-system-x86_64-headless.exe. Filtrar sólo qemu-system-x86_64.exe no detecta ese proceso y deja locks reales activos. No borrar locks sin comprobar todas las variantes del proceso y el AVD al que pertenecen. No usar wipe-data tras haber recibido datos; en este caso sólo se usó antes de instalar mPos en los AVD QA vacíos.

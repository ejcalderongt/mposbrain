# Entorno de laboratorio

AVD offline dedicado: mPos_Brain_Lab_10, 10 pulgadas, 1280x800, Android API 37. Paquete de contratos com.dtsgt.mpos.brainlab, runner AndroidJUnitRunner. Se compilan snapshots de commits en clones ignorados; no se modifica el checkout habitual.

Los APK offline no tienen permiso INTERNET, comprobado por aapt antes de instalar. Al primer intento, Firebase Installations intentó registrarse pese a tener desactivada la recolección y provocó una SecurityException por la ausencia del permiso. Ese intento fue fallo de infraestructura y no se contó como resultado de los contratos.

Corrección exclusiva de los contratos offline: retirar FirebaseInitProvider del manifest. No altera los cuatro mecanismos de propina. El segundo intento de guarded completó siete contratos con siete observaciones. Los detalles y hashes están en experiments/guarded.json. QA conserva la inicialización normal del SDK para el recorrido de actividades, con recolección desactivada por metadata.

Las pruebas sustituyen el encabezado dependiente de base y la impresora física, y extraen bloques de fuente para aspectos de Activity. El porcentaje recuperado se comprueba antes de cálculo completo. No demuestran un recorrido de UI completo, una impresión física ni la causa histórica del incidente del cliente.

El arranque limpio del primer AVD QA con imagen API 37.2 presentó fallos de componentes del sistema antes de ejecutar mPos. Se instaló adicionalmente system-images;android-35;google_apis;x86_64 para un AVD QA nuevo, mPos_Brain_QA_10_API35, puerto 5584. Esto no cambia la plataforma del contraste A/B, que fue API 37 para ambas variantes.

Para instalar la imagen se agregaron las herramientas oficiales de línea de comandos, verificando SHA-256 del ZIP contra la [página oficial de Android](https://developer.android.com/studio). La instalación vive bajo SDK/cmdline-tools/brain-23. El script conserva URL y hash verificados; no reemplaza una instalación existente.

Detalle de diagnóstico del host: con -no-window el ejecutable es qemu-system-x86_64-headless.exe. Filtrar sólo qemu-system-x86_64.exe no detecta ese proceso y deja locks reales activos. No borrar locks sin comprobar todas las variantes del proceso y el AVD al que pertenecen. No usar wipe-data tras haber recibido datos; en este caso sólo se usó antes de instalar mPos en los AVD QA vacíos.

En el primer arranque API 35, Android quedó en FallbackHome con device_provisioned=0 y user_setup_complete=0. Para el dispositivo de pruebas se completaron esos flags y se abrió HOME; sys.boot_completed pasó a 1. Esto configura Android, no la empresa ni la base de mPos. El runner espera boot_completed antes de instalar.

El primer inicio de instrumentación sufrió un ANR de startup. Se precompilaron ambos paquetes con cmd package compile -m speed -f. Después se observó SuperNotCalledException al intentar abrir MainActivity con FirebaseInitProvider retirado. Tras conservar la inicialización normal de Firebase en QA, se llegó a WSRec y comenzaron los despachos de recepción. No extrapolar la eliminación del provider de las pruebas de componentes a recorridos de UI.

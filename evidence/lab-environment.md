# Entorno de laboratorio

AVD offline dedicado: mPos_Brain_Lab_10, 10 pulgadas, 1280x800, Android API 37. Paquete de contratos com.dtsgt.mpos.brainlab, runner AndroidJUnitRunner. Se compilan snapshots de commits en clones ignorados; no se modifica el checkout habitual.

Los APK offline no tienen permiso INTERNET, comprobado por aapt antes de instalar. Al primer intento, Firebase Installations intentó registrarse pese a tener desactivada la recolección y provocó una SecurityException por la ausencia del permiso. Ese intento fue fallo de infraestructura y no se contó como resultado de los contratos.

Corrección exclusiva del laboratorio: retirar FirebaseInitProvider del manifest de todas las variantes. No altera los cuatro mecanismos de propina. El segundo intento de guarded completó siete contratos con siete observaciones. Los detalles y hashes están en experiments/guarded.json.

Las pruebas sustituyen el encabezado dependiente de base y la impresora física, y extraen bloques de fuente para aspectos de Activity. El porcentaje recuperado se comprueba antes de cálculo completo. No demuestran un recorrido de UI completo, una impresión física ni la causa histórica del incidente del cliente.

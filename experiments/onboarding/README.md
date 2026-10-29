# Alta QA observada

Requiere el AVD independiente mPos_Brain_QA_10 y la variante qa preparada/compilada. La fixture .local/qa-input.json contiene company, key y endpoint, sólo localmente. No usar un dispositivo de operación ni una base real compartida.

scripts/qa_run.py verifica el nombre del AVD y rechaza un arranque de base vacía si ya existe /sdcard/posdts.db. Instala el APK QA y el runner, transfiere temporalmente la fixture, abre MainActivity y espera que la aplicación abra WSRec por su propia detección de base vacía. Ingresa datos en los campos existentes y acciona doStart; no inserta pantallas intermedias.

El observer de scripts/qa_trace.py sólo añade números de callback y nombres de fase en el clon QA. Las huellas de UI sólo contienen ID/tipo/visibilidad/habilitación/posición de widgets. Nunca contienen texto de los campos ni contraseñas.

gl.estado_recep se vuelve true antes de validar parámetros y completar recepción adicional. Por eso el runner exige además observar el retorno de las validaciones finales. Ese retorno tampoco sustituye comprobar postcondiciones de tablas, caja, rol y navegación.

El runner guarda salida cruda privada y exporta únicamente estructuras permitidas. Elimina la fixture temporal del dispositivo al terminar. La base recibida queda privada para aprender el flujo; antes de pruebas de escrituras se debe hacer una copia y pasarla a un AVD offline.

No se invocan ventas, cobros, cierre fiscal ni envíos. Si hay selección de caja/sucursal o credencial de operador, observar y consultar al usuario; no inventar configuración.

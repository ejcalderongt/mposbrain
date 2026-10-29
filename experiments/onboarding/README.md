# Alta QA observada

Requiere el AVD independiente mPos_Brain_QA_10_API35 (puerto 5584) y la variante qa preparada/compilada. La fixture .local/qa-input.json contiene company, key y endpoint, sólo localmente. No usar un dispositivo de operación ni una base real compartida.

scripts/qa_run.py verifica el nombre del AVD y rechaza un arranque de base vacía si ya existe /sdcard/posdts.db. Instala el APK QA y el runner, transfiere temporalmente la fixture, abre MainActivity y espera que la aplicación abra WSRec por su propia detección de base vacía. Ingresa datos en los campos existentes y acciona doStart; no inserta pantallas intermedias.

Para reintentar después de un arranque fallido, --resume-empty conserva un snapshot privado y exige que P_EMPRESA, P_RUTA, P_SUCURSAL, T_VENTA y T_PAGO estén vacíos; nunca borra la base. Si ya hay recepción o datos operativos, se detiene.

El observer de scripts/qa_trace.py sólo añade números de callback y nombres de fase en el clon QA. Las huellas de UI sólo contienen ID/tipo/visibilidad/habilitación/posición de widgets. Nunca contienen texto de los campos ni contraseñas.

La fase callback se emite al entrar en execws; acredita despacho/selección de fase, no éxito de la respuesta SOAP. Algunas fases pueden no llamar al servicio o repetirse según las condiciones.

gl.estado_recep se vuelve true antes de validar parámetros y completar recepción adicional. Por eso el runner exige además observar el retorno de las validaciones finales. Ese retorno tampoco sustituye comprobar postcondiciones de tablas, caja, rol y navegación.

El runner guarda salida cruda privada y exporta únicamente estructuras permitidas. Elimina la fixture temporal del dispositivo al terminar. La base recibida queda privada para aprender el flujo; antes de pruebas de escrituras se debe hacer una copia y pasarla a un AVD offline.

No se invocan ventas, cobros, cierre fiscal ni envíos. Si hay selección de caja/sucursal o credencial de operador, observar y consultar al usuario; no inventar configuración.

## Segunda y tercera carga

El usuario enseñó que la primera carga recibe empresa; la segunda, perfil de ruta; la tercera, mesas. El perfil autorizado está en .local/qa-profile.json. Preparar el test con scripts/qa_stage_prepare.py, compilar QA y ejecutar scripts/qa_stage_run.py --stage 2; después --stage 3.

El test entra directamente a ConfigCaja en la etapa 2, selecciona IDs autorizados mediante sus Spinners y confirma el diálogo real. Después MainActivity recarga la configuración y WSRec usa los campos ya cargados. No hay UPDATE directo de Params desde el test ni inserción de 118. La etapa 3 exige que la ruta y 118 hayan quedado configurados previamente.

La entrada directa desde instrumentación no acredita login ni permisos de acceso al menú. Los estados antes/después contienen sólo booleanos y conteos de salas/mesas. Los mensajes de feedback capturados para resolver fallos de automatización permanecen en archivos privados; las huellas públicas siguen sin textos.

Cada intento nuevo conserva evidencia con timestamp; sólo un intento aprobado actualiza el alias qa-stageN.json y su esquema público. No reutilizar un fallo de confirmación como evidencia de que se ejecutó la recepción.

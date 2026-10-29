# Alta y sincronización

Estado: secuencia de código y recepción inicial observadas en QA. Proveniencia: checkout bd94c90c, MainActivity.initSession y WSRec; evidence/onboarding/qa-bootstrap.json.

1. MainActivity.initSession detecta dbVacia(), aplica actualización de estructura y abre WSRec con extra bd_vacia=true (líneas 521–541).
2. WSRec.onCreate inicializa PBase, toma conexión y parámetros; con base vacía habilita empresa/clave/URL. Hay comportamiento por país para carga de clientes.
3. doStart llama Recibir: valida campos, coloca empresa/clave/URL en AppGlobals, guarda URL y timeout en mposws.txt y comienza execws(1).
4. Primera llamada: GetP_EMPRESA. processEmpresas valida existencia/actividad y acumula SQL. Continúa GetP_ARCHIVOCONF, correlativos, descuentos, impuestos, clientes y otros catálogos mediante callbacks numerados. No todos los números son consecutivos ni todos los pasos se ejecutan bajo cualquier configuración.
5. processData ejecuta el script en transacción. validaParametros exige datos de P_SUCURSAL y P_RUTA. Después existen recepción adicional y finalización; no asumir listo para operar al terminar la primera llamada.

processConfig copia configuración recibida; processRutas copia cajas/rutas y sucursal. Los catálogos recibidos determinan navegación, permisos y comportamiento. Deben observarse los datos efectivos antes de diseñar un recorrido de restaurante.

Transporte: WebService.callMethod construye SOAP 1.1 y SOAPAction por método. Hallazgos para investigar: sustitución global de ampersand por Y al construir XML; manejo de errores HTTP y parseo. Son candidatos de riesgo, no causas confirmadas de la propina.

La base externa compartida exige AVD independiente. Las credenciales y respuestas SOAP completas nunca se incluyen en las huellas públicas. Una huella contiene identidad de pantalla, IDs, clase de widget, estructura, configuración no sensible y transición observada.

## Observación QA del 2026-10-29

La prueba Android pasó en API 35, en 104.011 segundos. MainActivity detectó la base vacía y abrió WSRec. Se ingresaron los datos privados mediante sus campos existentes y se accionó doStart. Se observaron despachos hasta la fase 63, transacción aplicada, entrada a finalización y retorno de sus validaciones; la última pantalla observada fue ValidCorel.

Se conservaron 33 huellas estructurales sin textos ni valores de inputs. El muestreo UI fue de un segundo: no acredita una captura por cada respuesta SOAP. Los marcadores callback son entradas a execws, no respuestas exitosas; algunos números se repiten o representan fases vacías.

La copia privada consistente posterior contiene 243 tablas, quick_check correcto y user_version=1. P_EMPRESA tiene una fila con país HN; hay una sucursal, doce cajas/rutas y sesenta registros de vendedores. Los catálogos P_RES_SALA y P_RES_MESA quedaron vacíos.

Configuración recibida y leída con lista permitida: P_PARAMEXT 117=S (propina fija), 120=10 (porcentaje), 207=S (confirmación). No existe 118; AppMethods.parametrosExtra usa false para peRest si falta. WSRec omite sala/mesa/grupo cuando peRest=false. No declarar listo el restaurante por el solo éxito de la recepción.

MantConfig.updateItem permite configurar localmente el parámetro 118 como “Modulo restaurante” (MantConfig.java:453,484). Antes de validar el recorrido operativo se requiere confirmar el perfil de caja/usuario y la activación esperada de QA. No se cambió esa configuración ni se generaron ventas o cobros.

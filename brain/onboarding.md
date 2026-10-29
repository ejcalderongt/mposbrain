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

La interpretación inicial de que faltaba habilitar Restaurante manualmente quedó corregida por enseñanza del usuario: el alta requiere tres cargas. La primera recibe empresa; la segunda usa la ruta configurada y recibe su perfil; sólo entonces se conoce que es restaurante, por lo que la tercera recibe salas/mesas. La ausencia de 118 tras la primera carga es compatible con ese flujo y no acredita una configuración defectuosa.

El usuario confirmó sucursal/caja; el perfil operativo está en .local/qa-profile.json. Se ejecutan las etapas restantes mediante ConfigCaja y WSRec, sin insertar manualmente 118. MantConfig puede modificar ese parámetro, pero hacerlo aquí sustituiría el procedimiento enseñado y perdería fidelidad. Login, rol de operador y recorrido de ventas siguen siendo validaciones separadas.

## Por qué son tres cargas en este código

WSRec.onCreate carga parametrosExtra antes de recibir. En wsExecute, las fases 37–39 comprueban ese peRest para elegir GetP_RES_SALA/MESA/GRUPO o callEmptyMethod. La fase 50, posterior a esas decisiones, sólo pide GetP_PARAMEXT_RUTA cuando codigo_ruta>0 (WSRec.java:459–461).

processParamExtRuta acumula un DELETE por ID y la inserción del valor de ruta, que sustituye al valor de empresa en el script. Esos valores se aplican en processData, después de recorrer las fases. No asumir que recibir 118 cambia peRest a mitad del mismo recorrido.

Por tanto: sin ruta en la primera carga no se obtiene ese perfil; con la ruta configurada en la segunda sí se obtiene, pero ya se tomaron las decisiones de salas/mesas; al recargar parámetros antes de la tercera se habilitan esas llamadas. Esta explicación combina el procedimiento enseñado con el orden concreto del código; las observaciones de etapas 2/3 deben acreditar sus transiciones.

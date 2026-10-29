# Alta y sincronización

Estado: secuencia leída en código, pendiente de observación completa en QA. Proveniencia: checkout bd94c90c, MainActivity.initSession y WSRec.

1. MainActivity.initSession detecta dbVacia(), aplica actualización de estructura y abre WSRec con extra bd_vacia=true (líneas 521–541).
2. WSRec.onCreate inicializa PBase, toma conexión y parámetros; con base vacía habilita empresa/clave/URL. Hay comportamiento por país para carga de clientes.
3. doStart llama Recibir: valida campos, coloca empresa/clave/URL en AppGlobals, guarda URL y timeout en mposws.txt y comienza execws(1).
4. Primera llamada: GetP_EMPRESA. processEmpresas valida existencia/actividad y acumula SQL. Continúa GetP_ARCHIVOCONF, correlativos, descuentos, impuestos, clientes y otros catálogos mediante callbacks numerados. No todos los números son consecutivos ni todos los pasos se ejecutan bajo cualquier configuración.
5. processData ejecuta el script en transacción. validaParametros exige datos de P_SUCURSAL y P_RUTA. Después existen recepción adicional y finalización; no asumir listo para operar al terminar la primera llamada.

processConfig copia configuración recibida; processRutas copia cajas/rutas y sucursal. Los catálogos recibidos determinan navegación, permisos y comportamiento. Deben observarse los datos efectivos antes de diseñar un recorrido de restaurante.

Transporte: WebService.callMethod construye SOAP 1.1 y SOAPAction por método. Hallazgos para investigar: sustitución global de ampersand por Y al construir XML; manejo de errores HTTP y parseo. Son candidatos de riesgo, no causas confirmadas de la propina.

La base externa compartida exige AVD independiente. Las credenciales y respuestas SOAP completas nunca se incluyen en las huellas públicas. Una huella contiene identidad de pantalla, IDs, clase de widget, estructura, configuración no sensible y transición observada.

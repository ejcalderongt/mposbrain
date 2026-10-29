# Recepción QA

Prueba real Android aprobada: emptyDatabaseOpensCommunicationAndReceivesQa. Duración 104.011 s, API 35. Artefacto sanitizado: qa-bootstrap.json. Las credenciales, base y salida cruda permanecen fuera de Git bajo .local.

Observado: base vacía → WSRec → despachos de recepción → transacción confirmada → validaciones finales retornadas → ValidCorel. Se guardaron 33 huellas de estructura de UI, sin textos ni inputs.

La copia posterior, capturada con el paquete detenido y sin WAL pendiente, pasó quick_check. Los archivos catalog/runtime-empty-schema.json y catalog/runtime-qa-schema.json contienen sólo esquema y conteos, sin filas ni defaults.

La recepción inicial no deja listo el restaurante: el usuario aclaró que son tres cargas sucesivas (empresa, perfil de ruta, mesas). La ausencia inicial de 118 explica peRest=false y no prueba un defecto de configuración. Se recibió propina fija de 10% y confirmación. Las siguientes etapas usan la caja autorizada, sin insertar manualmente parámetros ni emitir documentos.

Segunda carga aprobada: qa-stage2.json contiene 32 huellas y los estados antes/después. El perfil coincide con el autorizado; peRest cambia de false a true, aparece 118=S y salas/mesas permanecen vacíos. La entrada a ConfigCaja y WSRec desde el test no valida login ni permisos de menú. Los intentos previos que no llegaron a recibir datos se conservan por separado y no cuentan como cargas completadas.

Tercera carga aprobada: qa-stage3.json contiene 29 huellas. Antes: Restaurante activo y salas/mesas en cero. Después: Restaurante sigue activo y se recibieron 1 sala y 133 mesas. El snapshot pasó quick_check y está descrito en catalog/runtime-qa-stage3-schema.json. La cifra incluye el catálogo recibido completo; no implica 133 mesas activas o recorridas.

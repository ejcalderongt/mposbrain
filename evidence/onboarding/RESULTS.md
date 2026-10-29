# Recepción QA

Prueba real Android aprobada: emptyDatabaseOpensCommunicationAndReceivesQa. Duración 104.011 s, API 35. Artefacto sanitizado: qa-bootstrap.json. Las credenciales, base y salida cruda permanecen fuera de Git bajo .local.

Observado: base vacía → WSRec → despachos de recepción → transacción confirmada → validaciones finales retornadas → ValidCorel. Se guardaron 33 huellas de estructura de UI, sin textos ni inputs.

La copia posterior, capturada con el paquete detenido y sin WAL pendiente, pasó quick_check. Los archivos catalog/runtime-empty-schema.json y catalog/runtime-qa-schema.json contienen sólo esquema y conteos, sin filas ni defaults.

La recepción inicial no dejó listo el restaurante: falta P_PARAMEXT 118, el código cae a peRest=false y omite catálogos de salas/mesas. Sí recibió propina fija de 10% y confirmación. Se pidió al usuario el perfil de caja/rol y cómo corresponde habilitar Restaurante en QA; no se inventó una configuración ni se emitieron documentos.

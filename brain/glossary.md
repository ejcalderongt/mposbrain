# Glosario inicial

| Término | Significado observado en código |
|---|---|
| gl | appGlobals: estado mutable compartido entre actividades |
| ruta / codigo_ruta | También representa caja/configuración de operación; no asumir ruta logística |
| mesa | Contexto de sala y atención; puede tener varias cuentas |
| cuenta | Agrupación que se precuenta/cobra; correlacionar con orden y mesa |
| precuenta | Presentación e impresión previas al documento final |
| FacturaRes.monto_propina | Porcentaje local: recibe pePropinaPerc en onCreate y se divide entre 100 en calculate |
| gl.monto_propina | Importe monetario global: fillTotals lo asigna desde propina; no equivale al campo local homónimo |
| propina / propinaext | Importes monetarios calculado y extra en FacturaRes |
| propinaperc | Porcentaje que acompaña la propina calculada/persistida |
| propina_vacia | Existen banderas local y global; no son intercambiables |
| propfija / pePropinaFija | Configuración de cálculo/representación de propina |
| footerBaseGUA | Implementación compartida de footer de precuenta, invocada también para Honduras |
| buildPrint | Construcción/guardado del documento; éxito no equivale a impresión física exitosa |
| WSRec / WSEnv | Recepción / envío SOAP; pueden existir integraciones Firebase y otras además de estas pantallas |
| posdts.db | SQLite externa compartida por aplicaciones en el mismo dispositivo |

Las definiciones se refinarán con la configuración recibida y la enseñanza del operador. No equiparar nombres parecidos sin seguir asignaciones y consumidores.

Proveniencia de unidades: FacturaRes.java, bd94c90c, líneas 375, 1012–1018 y 1176. No sumar ni comparar directamente el porcentaje local con el importe global.

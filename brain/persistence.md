# Persistencia de restaurante y propina

Estado: código bd94c90c, esquema efectivo pendiente de consultar tras recepción QA.

FacturaRes.saveOrder (1551–2915) escribe mediante handlers, además de SQL directo. Por eso la lista de tablas inferidas de literales dentro del método no es un análisis de impacto completo. Seguir también objetos clsD_* y sus métodos add/update.

La propina se registra en D_FACTURAPR mediante clsD_facturaprObj.add. FacturaRes construye empresa, correlativo, sucursal, vendedor, fecha, PROPINA, PROPPERC y PROPEXTRA (2328–2364). El handler asigna esos campos a la inserción; no asumir que todos viven en D_FACTURA.

El bloque está condicionado por propina>0. Dentro se redondea el importe y existe recuperación desde gl.monto_propina si después del redondeo queda cero. Esta recuperación no protege una entrada que ya era cero antes de la condición exterior. Es una observación de código, no una nueva causa confirmada: cero también puede ser legítimo por exclusiones. Investigar con trazas antes de añadir una recuperación que pudiera cobrar propina indebidamente.

Con pagocarta y pePropinaCarta, el importe/porcentaje persistido puede ajustarse respecto al monto calculado. La conciliación debe conocer ese modo; no declarar corrupción sólo porque dos montos difieren.

El registro de precuenta usa D_PRECUENTA_ENC, D_PRECUENTA_DET y D_PRECUENTA_FACTURA. El catálogo DDL contiene candidatos de estructura y su hash. Comprobar schema_version, PRAGMA table_info y versión de BaseDatosVersion en la copia recibida antes de diseñar consultas de validación.

Para una prueba end-to-end, correlacionar fixture de mesa/cuenta → T_VENTA/T_PAGO → documento/correlativo → D_FACTURAPR y registro de precuenta. Verificar begin/setSuccessful/end y excepciones; los handlers pueden ocultar errores y deben incluirse en la evidencia de persistencia.

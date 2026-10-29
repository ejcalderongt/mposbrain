# Incidente de propina

Reporte del usuario: Honduras; una misma cuenta puede producir distintas representaciones de propina. Evidencia de cliente recibida por capturas; no permite inferir por sí sola qué ruta de código se ejecutó.

## Cuatro mecanismos candidatos

| Mecanismo | Antes | Blindaje | Alcance de prueba |
|---|---|---|---|
| Mutación al imprimir sin propina | FacturaRes.impresionCuenta resta propina al total y pone el campo en cero | Proyección inmutable PrecuentaValues | Alternar sin/con en modelo sintético |
| Bandera global heredada | onCreate puede inicializar porcentaje en cero por gl.propina_vacia; aceptación explícita sólo cambia bandera local | Recuperar porcentaje configurado respetando exclusiones | Bloques extraídos de fuente; cálculo completo pendiente |
| Totales omitidos | clsDocCuenta.footerBaseGUA depende de descuento o propina fija | Emitir totales y reconocer monto variable positivo | Generador real de footer con importes sintéticos |
| Archivo previo despachado | clsDocument.buildPrint puede reportar éxito tras excepción; llamador ignora resultado | Resultado false y bloqueo del despacho/actualizaciones | Excepción y fallo de guardado inyectados, impresora doble |

Los matches de guardas indican que una condición candidata apareció. No demuestran automáticamente la causa del incidente histórico. Correlacionar cuenta/sesión, estado antes/después y documento producido.

La función buildFooter llama incondicionalmente a footerBaseGUA, también para Honduras. No descartar esta ruta por su nombre. La configuración propina fija/variable, llevar/domicilio/sin_propina y porcentaje real deben formar parte del escenario.

El experimento A/B compara bd94c90c con c21e92ec. Este último también precede a la reubicación del menú: diferencia conocida ajena a los contratos. No hay parche aplicado al checkout habitual ni rollback sobre datos reales.

# Instrucciones para agentes de mPos

Lee HANDOFF.md y brain/INDEX.md antes de modificar o diagnosticar. Este brain no es el checkout de la aplicación. Descubre su ruta local y comprueba rama, commit y cambios sin guardar; nunca descartes cambios del usuario.

## Evidencia y aprendizaje

- Etiqueta cada afirmación: código, ejecución, reporte del usuario o hipótesis.
- Conserva archivo, símbolo, línea y commit. Las líneas sin commit caducan.
- Un grafo de Intent no equivale a un recorrido observado. Un contrato con dobles no equivale a un recibo de una impresora física.
- Registra país, configuración, rol, estado anterior, acción, estado posterior, evidencia y límite de cobertura.
- Usa templates/learning.md para incorporar aprendizaje. Conserva hipótesis descartadas con su razón.
- Al cerrar un incidente exige reproducción, explicación causal, contraste antes/después y controles de regresión; documenta lo que no se pudo probar.

## Aislamiento

La base posdts.db vive en almacenamiento externo compartido. Otro applicationId no basta para aislarla. Usa un AVD dedicado y verifica su nombre antes de instalar, limpiar o reemplazar una base.

Las pruebas de rollback no tienen permiso INTERNET y no usan datos reales. La sincronización QA está autorizada para el alta y recepción; no implica autorización para ventas, FEL, cobros ni envíos operativos.

No versiones claves, archivos SQLite, SOAP crudo, URLs con credenciales, Google Services, llaves de firma, capturas con datos de personas ni volcados sin filtrar. Los insumos privados viven en .local. No registres textos de EditText ni hashes de contraseñas de baja entropía.

## Impresión y propina

En Honduras la precuenta usa footerBaseGUA(); el nombre no delimita el país. Comprueba el llamador antes de concluir alcance regional. Sigue monto, porcentaje, exclusiones, banderas locales/globales, modelo, proyección de impresión, archivo generado y despacho por separado.

No añadas pantallas al flujo para diagnosticar. Las utilidades de diagnóstico están agrupadas en el menú principal, Utilerías.

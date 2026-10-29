# Leer trazas y producir una huella

Proveniencia: bd94c90c, DiagnosticLog, RollingTraceFile y FacturaRes.tracePropina.

La aplicación ya registra ciclos de vida de todas las actividades y snapshots específicos de FacturaRes. Los archivos están bajo el directorio privado externo de la aplicación, diagnostics/verbose-current.jsonl y sus rotaciones. Límite configurado: 1 MiB por archivo, tres archivos. La cola es finita y reporta droppedSoFar; ausencia de un evento no prueba ausencia de ejecución.

Cada registro incluye sesión, secuencia, tiempo UTC/monotónico, versión, evento y contexto operativo. Los snapshots de FacturaRes distinguen modelo y representación: propina, porcentaje, monto, total, banderas local/global, filas de totales, altura y posiciones visibles. Un driver que retorna no confirma impresión física.

## Procedimiento

1. Extraer snapshot mediante Utilerías o ADB autorizado; mantener el original en .local.
2. Conservar orden y sesiones. Si se combinan rotaciones, hacerlo de antigua a nueva y detectar duplicados/gaps.
3. Ejecutar scripts/trace_analyze.py <entrada> --output <reporte>. El resumen omite identificadores de cuenta/sesión y valores de campos; conserva conteos de eventos, matches, discrepancias y transiciones observadas.
4. Buscar el evento en catalog/trace_events.jsonl para llegar a su símbolo/línea y contrastar el commit.
5. Para una causa concreta, revisar privadamente la secuencia de esa cuenta: configuración → cálculo → exclusiones → filas → argumentos → generación → despacho → persistencia. Publicar sólo evidencia sanitizada necesaria.

Los eventos tip_guard_*_match permiten detectar coincidencias con candidatos. rowMissing y stateDiffersFromRendered son observaciones, no incidentes únicos ni necesariamente errores: pueden aparecer antes de rebind/layout. Correlacionar con totals_bound y totals_after_layout.

Los ciclos de vida producen una huella de pantallas reanudadas; incluyen regresos y no equivalen a aristas Intent directas. Las huellas UI del runner QA agregan estructura de widgets sin textos. La captura completa con textos o base de datos permanece privada.

Firebase de diagnóstico es una vía de extracción existente; los contratos offline deshabilitan la inicialización del SDK y carecen de INTERNET. Las observaciones QA de fases no contienen SOAP ni credenciales.

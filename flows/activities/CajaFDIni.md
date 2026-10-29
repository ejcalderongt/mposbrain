# CajaFDIni

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CajaFDIni.java:24`; hereda `PBase`.

## Layouts candidatos

- `activity_caja_fdini` — `app/src/main/java/com/dtsgt/mpos/CajaFDIni.java:49`.

## Navegación candidata

- `FELVerificacion` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaFDIni.java:85`; condiciones en catálogo.
- `CajaPagosPend` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaFDIni.java:126`; condiciones en catálogo.
- `WSRec` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaFDIni.java:355`; condiciones en catálogo.

## Estado global escrito

`corelZ`, `felcorel`, `feluuid`, `inicia_caja_primera_vez`, `inicio_caja_correcto`, `recibir_automatico`, `servidor_anio`

## Tablas mencionadas estáticamente

`D_FACTURA`, `T_BARRA_BONIF`

## Métodos

- `onCreate` — línea 45.
- `save` — línea 103.
- `doExit` — línea 120.
- `pendiente` — línea 124.
- `doFondoClick` — línea 129.
- `doEfectClick` — línea 133.
- `setHandlers` — línea 140.
- `guardar` — línea 158.
- `saveMontoIni` — línea 177.
- `validacionesInicio` — línea 257.
- `checkDate` — línea 285.
- `dateCallback` — línea 300.
- `msgAskExit` — línea 340.
- `msgAskSend` — línea 370.
- `msgAskFechaIni` — línea 385.
- `msgAskNoFecha` — línea 397.
- `msgText` — línea 409.
- `inputValorFondo` — línea 423.
- `onClick` — línea 430.
- `onClick` — línea 437.
- `inputValorEfect` — línea 451.
- `onClick` — línea 458.
- `validaFacturas` — línea 476.
- `validaPendiente` — línea 503.
- `writeCorelLog` — línea 507.
- `pendienteFEL` — línea 516.
- `pendienteFELHoy` — línea 542.
- `onResume` — línea 560.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

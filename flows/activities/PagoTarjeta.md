# PagoTarjeta

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/PagoTarjeta.java:31`; hereda `PBase`.

## Layouts candidatos

- `activity_pago_tarjeta` — `app/src/main/java/com/dtsgt/mpos/PagoTarjeta.java:54`.

## Navegación candidata

- `Cupon` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PagoTarjeta.java:311`; condiciones en catálogo.
- `Cupon` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PagoTarjeta.java:336`; condiciones en catálogo.
- `BilleteraPago` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PagoTarjeta.java:343`; condiciones en catálogo.
- `com.mposbac.test` (external_app_candidate) — `app/src/main/java/com/dtsgt/mpos/PagoTarjeta.java:410`; condiciones en catálogo.

## Estado global escrito

`codigo_cliente`, `mediapago_cupon`, `modo_cortesia`, `monto_cupon`

## Tablas mencionadas estáticamente

`D_FACTURA`, `D_FACTURAP`, `D_PAGO_BAC`, `T_PAGO`

## Métodos

- `onCreate` — línea 50.
- `doSave` — línea 85.
- `doExit` — línea 89.
- `doList` — línea 93.
- `setHandlers` — línea 97.
- `onKey` — línea 102.
- `onEditorAction` — línea 113.
- `save` — línea 156.
- `listaTipos` — línea 236.
- `onItemClick` — línea 276.
- `onClick` — línea 369.
- `ejecutaCredomatic` — línea 387.
- `procesaCredomatic` — línea 422.
- `confirmaPago` — línea 473.
- `rechazaPago` — línea 485.
- `saveCredomatic` — línea 497.
- `saveBrazalete` — línea 565.
- `procesaBrazalete` — línea 632.
- `validaPagoCupon` — línea 679.
- `eliminarPagoCupon` — línea 691.
- `round2` — línea 702.
- `msgAskExit` — línea 720.
- `onClick` — línea 727.
- `msgAskCupon` — línea 738.
- `onClick` — línea 745.
- `onClick` — línea 751.
- `onResume` — línea 762.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

# Cobro

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/Cobro.java:34`; hereda `PBase`.

## Layouts candidatos

- `activity_cobro` — `app/src/main/java/com/dtsgt/mpos/Cobro.java:62`.

## Navegación candidata

- `Pago` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Cobro.java:160`; condiciones en catálogo.
- `Pago` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Cobro.java:268`; condiciones en catálogo.
- `Aprofam1` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Cobro.java:557`; condiciones en catálogo.

## Estado global escrito

`brw`, `facturaVen`, `pagocobro`, `pagolim`, `pagomodo`, `pagoval`, `validarCred`

## Tablas mencionadas estáticamente

`D_COBRO`, `D_COBROD`, `D_FACTURA`, `P_CLIENTE`, `P_COBRO`, `T_PAGO`, `T_PAGOD`

## Métodos

- `onCreate` — línea 59.
- `run` — línea 95.
- `run` — línea 101.
- `run` — línea 117.
- `paySelect` — línea 141.
- `payCash` — línea 170.
- `checkAll` — línea 190.
- `check` — línea 202.
- `sinRef` — línea 257.
- `setHandlers` — línea 277.
- `onCheckedChanged` — línea 282.
- `onCheckedChanged` — línea 289.
- `onItemClick` — línea 297.
- `onCheckedChanged` — línea 323.
- `listItems` — línea 339.
- `doExit` — línea 394.
- `validaCredito` — línea 402.
- `msgAskFact` — línea 482.
- `onClick` — línea 524.
- `onClick` — línea 541.
- `initVenta` — línea 554.
- `createDoc` — línea 568.
- `sfecha` — línea 628.
- `saveCobro` — línea 644.
- `docList` — línea 828.
- `applyPay` — línea 868.
- `inputEfectivo` — línea 934.
- `onClick` — línea 955.
- `onClick` — línea 964.
- `checkCash` — línea 978.
- `singlePrint` — línea 1030.
- `showTotals` — línea 1040.
- `calcSelected` — línea 1065.
- `clearAll` — línea 1119.
- `getDocPago` — línea 1130.
- `initSession` — línea 1159.
- `askPrint` — línea 1177.
- `onClick` — línea 1187.
- `onClick` — línea 1246.
- `exit` — línea 1263.
- `msgAskOverPayd` — línea 1283.
- `onClick` — línea 1295.
- `onClick` — línea 1301.
- `msgAskSave` — línea 1314.
- `onClick` — línea 1328.
- `onClick` — línea 1336.
- `msgAskExit` — línea 1349.
- `onClick` — línea 1362.
- `onClick` — línea 1368.
- `onResume` — línea 1384.
- `onBackPressed` — línea 1415.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

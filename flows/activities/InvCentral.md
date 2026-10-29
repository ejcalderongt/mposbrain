# InvCentral

Dominio: `inventory`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/InvCentral.java:34`; hereda `PBase`.

## Layouts candidatos

- `activity_inv_central` — `app/src/main/java/com/dtsgt/mpos/InvCentral.java:65`.

## Navegación candidata

- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvCentral.java:649`; condiciones en catálogo.
- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvCentral.java:800`; condiciones en catálogo.

## Estado global escrito

`autocom`

## Tablas mencionadas estáticamente

`D_MOVD`, `D_MOVD_ALMACEN`, `P_STOCK`, `P_STOCK_INVENTARIO_DET`, `P_STOCK_INVENTARIO_ENC`, `P_STOCK_INV_DET`, `P_STOCK_INV_ERR`

## Métodos

- `onCreate` — línea 61.
- `run` — línea 116.
- `doApply` — línea 131.
- `doPrint` — línea 135.
- `doCancel` — línea 139.
- `setHandlers` — línea 143.
- `onItemClick` — línea 147.
- `listItems` — línea 163.
- `saveInventory` — línea 220.
- `callbackInvCent` — línea 260.
- `requestInventory` — línea 281.
- `applyInventory` — línea 294.
- `aplicarInventario` — línea 302.
- `aplicarInventarioAlmacen` — línea 430.
- `addtoStock` — línea 545.
- `addtoStockOld` — línea 567.
- `logError` — línea 599.
- `showInvErrors` — línea 613.
- `enviaEstado` — línea 636.
- `imprimirInventario` — línea 658.
- `setDatosVersion` — línea 691.
- `msgAskAplicar` — línea 707.
- `msgAskAplicar2` — línea 726.
- `msgAskCancelar` — línea 748.
- `msgAskExit` — línea 770.
- `msgAskOK` — línea 791.
- `msgAskImprimir` — línea 811.
- `onResume` — línea 831.
- `onBackPressed` — línea 842.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

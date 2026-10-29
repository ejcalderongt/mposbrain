# PedidoRes

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/PedidoRes.java:34`; hereda `PBase`.

## Layouts candidatos

- `activity_pedido_res` — `app/src/main/java/com/dtsgt/mpos/PedidoRes.java:69`.

## Navegación candidata

- `BonVenta` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidoRes.java:122`; condiciones en catálogo.
- `DescBon` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidoRes.java:159`; condiciones en catálogo.

## Estado global escrito

`brw`, `promcant`, `promdesc`, `promprod`

## Tablas mencionadas estáticamente

`D_PEDIDO`, `P_CLIENTE`, `T_BONITEM`, `T_VENTA`

## Métodos

- `onCreate` — línea 66.
- `run` — línea 102.
- `run` — línea 108.
- `showBon` — línea 121.
- `processFinalPromo` — línea 129.
- `run` — línea 140.
- `showPromo` — línea 152.
- `updDesc` — línea 168.
- `totalOrder` — línea 179.
- `fillTotals` — línea 213.
- `finishOrder` — línea 283.
- `singlePrint` — línea 313.
- `saveOrder` — línea 317.
- `totalDescProd` — línea 417.
- `saveAtten` — línea 440.
- `showDateDialog` — línea 488.
- `obtenerFecha` — línea 499.
- `onDateSet` — línea 502.
- `setActDate` — línea 518.
- `adjustSpinner` — línea 534.
- `onItemSelected` — línea 538.
- `onNothingSelected` — línea 559.
- `fillSpinner` — línea 572.
- `askSave` — línea 601.
- `onClick` — línea 608.
- `setDate` — línea 623.
- `checkPromo` — línea 627.
- `askPrint` — línea 641.
- `onClick` — línea 647.
- `onClick` — línea 680.
- `onResume` — línea 699.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

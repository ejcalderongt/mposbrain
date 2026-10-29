# PedidosEnv

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/PedidosEnv.java:32`; hereda `PBase`.

## Layouts candidatos

- `activity_pedidos_envv` — `app/src/main/java/com/dtsgt/mpos/PedidosEnv.java:57`.

## Navegación candidata

- `PedidoEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidosEnv.java:124`; condiciones en catálogo.
- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidosEnv.java:359`; condiciones en catálogo.
- `srvPedidosBitacora` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidosEnv.java:481`; condiciones en catálogo.
- `ValidaSuper` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidosEnv.java:553`; condiciones en catálogo.

## Estado global escrito

`checksuper`, `closePedido`, `pedid`

## Tablas mencionadas estáticamente

`D_PEDIDO`, `D_PEDIDOC`, `D_PEDIDOCOM`, `D_PEDIDOCOMBO`, `D_PEDIDOD`, `D_PEDIDOORDEN`, `P_PRODUCTO`

## Métodos

- `onCreate` — línea 54.
- `doMenu` — línea 99.
- `doExit` — línea 103.
- `doRefresh` — línea 107.
- `setHandlers` — línea 112.
- `onItemClick` — línea 115.
- `listItems` — línea 134.
- `iniciaPedidos` — línea 210.
- `run` — línea 214.
- `run` — línea 216.
- `cancelaPedidos` — línea 225.
- `recibePedidos` — línea 231.
- `wsCallBack` — línea 263.
- `procesaEstados` — línea 275.
- `aplicaEstados` — línea 289.
- `enviaConfirmacion` — línea 357.
- `statistics` — línea 372.
- `updateStats` — línea 425.
- `syncStat` — línea 457.
- `statTPPO` — línea 492.
- `limitePedido` — línea 505.
- `pantallaHorizontal` — línea 524.
- `showItemMenu` — línea 538.
- `onItemClick` — línea 547.
- `onClick` — línea 563.
- `msgAskDelete` — línea 576.
- `onClick` — línea 582.
- `onClick` — línea 588.
- `msgAskDelete2` — línea 595.
- `onClick` — línea 601.
- `onClick` — línea 625.
- `onResume` — línea 636.
- `onPause` — línea 666.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

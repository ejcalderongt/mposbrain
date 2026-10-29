# Pedidos

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/Pedidos.java:30`; hereda `PBase`.

## Layouts candidatos

- `activity_pedidos` — `app/src/main/java/com/dtsgt/mpos/Pedidos.java:56`.
- `activity_pedidos_ver` — `app/src/main/java/com/dtsgt/mpos/Pedidos.java:58`.

## Navegación candidata

- `PedidoDet` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Pedidos.java:124`; condiciones en catálogo.
- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Pedidos.java:362`; condiciones en catálogo.
- `srvPedidosBitacora` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Pedidos.java:484`; condiciones en catálogo.
- `ValidaSuper` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Pedidos.java:565`; condiciones en catálogo.

## Estado global escrito

`checksuper`, `closePedido`, `pedid`

## Tablas mencionadas estáticamente

`D_PEDIDO`, `D_PEDIDOC`, `D_PEDIDOCOM`, `D_PEDIDOCOMBO`, `D_PEDIDOD`, `D_PEDIDOORDEN`, `P_PRODUCTO`

## Métodos

- `onCreate` — línea 52.
- `doMenu` — línea 99.
- `doExit` — línea 103.
- `doRefresh` — línea 107.
- `setHandlers` — línea 112.
- `onItemClick` — línea 115.
- `listItems` — línea 134.
- `iniciaPedidos` — línea 208.
- `run` — línea 212.
- `run` — línea 214.
- `cancelaPedidos` — línea 223.
- `recibePedidos` — línea 229.
- `wsCallBack` — línea 264.
- `procesaEstados` — línea 277.
- `aplicaEstados` — línea 291.
- `enviaConfirmacion` — línea 360.
- `statistics` — línea 375.
- `updateStats` — línea 428.
- `syncStat` — línea 460.
- `statTPPO` — línea 495.
- `limitePedido` — línea 508.
- `pantallaHorizontal` — línea 527.
- `showItemMenu` — línea 541.
- `onItemClick` — línea 553.
- `onClick` — línea 573.
- `msgAskDelete` — línea 587.
- `onClick` — línea 593.
- `onClick` — línea 599.
- `msgAskDelete2` — línea 606.
- `onClick` — línea 612.
- `onClick` — línea 636.
- `onResume` — línea 647.
- `onPause` — línea 677.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

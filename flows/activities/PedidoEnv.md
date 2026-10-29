# PedidoEnv

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/PedidoEnv.java:45`; hereda `PBase`.

## Layouts candidatos

- `activity_pedido_env` — `app/src/main/java/com/dtsgt/mpos/PedidoEnv.java:87`.
- `activity_pedido_env` — `app/src/main/java/com/dtsgt/mpos/PedidoEnv.java:89`.

## Navegación candidata

- `PedidoCli` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidoEnv.java:167`; condiciones en catálogo.
- `ValidaSuper` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidoEnv.java:177`; condiciones en catálogo.
- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidoEnv.java:434`; condiciones en catálogo.
- `srvPedidoEstado` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidoEnv.java:450`; condiciones en catálogo.

## Estado global escrito

`checksuper`, `closePedido`, `codigo_cliente`, `gCorreoCliente`, `gDirCliente`, `gNITCliente`, `gNombreCliente`, `iniciaVenta`, `pedcorel`, `sin_propina`, `ventalock`

## Tablas mencionadas estáticamente

`D_FACTURA`, `D_FACTURAP`, `D_PEDIDO`, `D_PEDIDOD`, `T_COMANDA`, `T_COMBO`, `T_PAGO`, `T_PRODMENU`, `T_VENTA`

## Métodos

- `onCreate` — línea 83.
- `doNuevo` — línea 130.
- `doPend` — línea 135.
- `doComp` — línea 140.
- `doEnt` — línea 148.
- `doPago` — línea 153.
- `doDel` — línea 162.
- `doCliente` — línea 166.
- `doAnul` — línea 170.
- `doExit` — línea 183.
- `setHandlers` — línea 187.
- `onItemClick` — línea 190.
- `listItems` — línea 209.
- `loadItem` — línea 283.
- `estado` — línea 348.
- `broadCast` — línea 406.
- `anular` — línea 445.
- `aplicarPago` — línea 465.
- `crearVenta` — línea 480.
- `crearTicketEntrega` — línea 524.
- `addItem` — línea 591.
- `imprimirOrden` — línea 663.
- `imprimeComanda` — línea 704.
- `divideComanda` — línea 710.
- `agregaComanda` — línea 777.
- `generaArchivos` — línea 792.
- `wsCallBack` — línea 886.
- `cargaDetallePedido` — línea 897.
- `agregaDetallePedido` — línea 911.
- `getProd` — línea 982.
- `bigtoast` — línea 994.
- `ventaVacia` — línea 1009.
- `borrarVenta` — línea 1023.
- `iniciaTiempo` — línea 1046.
- `run` — línea 1049.
- `run` — línea 1051.
- `cancelaTiempo` — línea 1060.
- `actualizaTiempo` — línea 1066.
- `montoPago` — línea 1071.
- `splitByLen` — línea 1084.
- `pantallaHorizontal` — línea 1094.
- `addItemSqlAndroid` — línea 1104.
- `addItemPedidoCom` — línea 1131.
- `msgAsk` — línea 1148.
- `onClick` — línea 1154.
- `onClick` — línea 1160.
- `msgAskAnul` — línea 1167.
- `onClick` — línea 1173.
- `onClick` — línea 1179.
- `msgAskAnul2` — línea 1186.
- `onClick` — línea 1192.
- `onClick` — línea 1198.
- `msgAskDel` — línea 1205.
- `onClick` — línea 1211.
- `onClick` — línea 1222.
- `msgAskPago` — línea 1229.
- `onClick` — línea 1235.
- `onClick` — línea 1241.
- `onResume` — línea 1253.
- `onPause` — línea 1281.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

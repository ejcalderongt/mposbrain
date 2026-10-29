# PedidoDet

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/PedidoDet.java:45`; hereda `PBase`.

## Layouts candidatos

- `activity_pedido_det` — `app/src/main/java/com/dtsgt/mpos/PedidoDet.java:88`.
- `activity_pedido_det_ver` — `app/src/main/java/com/dtsgt/mpos/PedidoDet.java:90`.

## Navegación candidata

- `PedidoCli` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidoDet.java:198`; condiciones en catálogo.
- `ValidaSuper` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidoDet.java:208`; condiciones en catálogo.
- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidoDet.java:497`; condiciones en catálogo.
- `srvPedidoEstado` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidoDet.java:515`; condiciones en catálogo.

## Estado global escrito

`checksuper`, `closePedido`, `codigo_cliente`, `gCorreoCliente`, `gDirCliente`, `gNITCliente`, `gNombreCliente`, `iniciaVenta`, `pedcorel`, `sin_propina`, `ventalock`

## Tablas mencionadas estáticamente

`D_FACTURA`, `D_FACTURAP`, `D_PEDIDOD`, `T_COMANDA`, `T_COMBO`, `T_PAGO`, `T_PRODMENU`, `T_VENTA`

## Métodos

- `onCreate` — línea 83.
- `doNuevo` — línea 151.
- `doPend` — línea 156.
- `doComp` — línea 161.
- `doEnt` — línea 181.
- `doPago` — línea 186.
- `doCliente` — línea 197.
- `doAnul` — línea 201.
- `doExit` — línea 214.
- `setHandlers` — línea 218.
- `onItemClick` — línea 221.
- `listItems` — línea 240.
- `loadItem` — línea 315.
- `estado` — línea 391.
- `broadCast` — línea 468.
- `anular` — línea 508.
- `aplicarPago` — línea 530.
- `crearVenta` — línea 545.
- `crearTicketEntrega` — línea 591.
- `addItem` — línea 659.
- `imprimirOrden` — línea 728.
- `imprimeComanda` — línea 769.
- `divideComanda` — línea 775.
- `agregaComanda` — línea 843.
- `generaArchivos` — línea 858.
- `wsCallBack` — línea 945.
- `cargaDetallePedido` — línea 956.
- `agregaDetallePedido` — línea 971.
- `getProd` — línea 1046.
- `bigtoast` — línea 1058.
- `ventaVacia` — línea 1073.
- `borrarVenta` — línea 1087.
- `iniciaTiempo` — línea 1110.
- `run` — línea 1113.
- `run` — línea 1115.
- `cancelaTiempo` — línea 1124.
- `actualizaTiempo` — línea 1130.
- `montoPago` — línea 1147.
- `splitByLen` — línea 1176.
- `pantallaHorizontal` — línea 1186.
- `addItemSqlAndroid` — línea 1196.
- `addItemPedidoCom` — línea 1223.
- `msgAsk` — línea 1240.
- `onClick` — línea 1246.
- `onClick` — línea 1252.
- `msgAskAnul` — línea 1259.
- `onClick` — línea 1265.
- `onClick` — línea 1271.
- `msgAskAnul2` — línea 1278.
- `onClick` — línea 1284.
- `onClick` — línea 1290.
- `msgAskVenta` — línea 1297.
- `onClick` — línea 1303.
- `onClick` — línea 1309.
- `msgAskPago` — línea 1316.
- `onClick` — línea 1322.
- `onClick` — línea 1328.
- `onResume` — línea 1340.
- `onPause` — línea 1368.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

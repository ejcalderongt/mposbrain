# PedidoEnviar

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/PedidoEnviar.java:49`; hereda `PBase`.

## Layouts candidatos

- `activity_pedido_enviar` — `app/src/main/java/com/dtsgt/mpos/PedidoEnviar.java:94`.
- `activity_pedido_enviar_ver` — `app/src/main/java/com/dtsgt/mpos/PedidoEnviar.java:96`.

## Navegación candidata

- `PedidoCli` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidoEnviar.java:165`; condiciones en catálogo.
- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidoEnviar.java:530`; condiciones en catálogo.

## Estado global escrito

`checksuper`, `closePedido`, `codigo_cliente`, `gCorreoCliente`, `gDirCliente`, `gNITCliente`, `gNombreCliente`, `iniciaVenta`, `pedcorel`, `ventalock`

## Tablas mencionadas estáticamente

`D_FACTURA`, `D_FACTURAP`, `D_PEDIDO`, `D_PEDIDOC`, `D_PEDIDOD`, `D_PEDIDOORDEN`, `T_COMANDA`, `T_COMBO`, `T_PAGO`, `T_PRODMENU`, `T_VENTA`

## Métodos

- `onCreate` — línea 89.
- `run` — línea 137.
- `doPend` — línea 151.
- `doRePrint` — línea 156.
- `doReSend` — línea 160.
- `doCliente` — línea 164.
- `doExit` — línea 168.
- `setHandlers` — línea 172.
- `onItemClick` — línea 175.
- `listItems` — línea 194.
- `parseNote` — línea 265.
- `loadItem` — línea 294.
- `estado` — línea 329.
- `aplicarPago` — línea 354.
- `enviaOrden` — línea 365.
- `addItemSqlNoImage` — línea 410.
- `addItemSqlAndroid` — línea 437.
- `addOrdenItemSql` — línea 463.
- `confirmaEnvio` — línea 476.
- `broadCast` — línea 494.
- `crearVenta` — línea 545.
- `crearTicketEntrega` — línea 587.
- `addItem` — línea 654.
- `imprimirOrden` — línea 726.
- `imprimeComanda` — línea 753.
- `divideComanda` — línea 759.
- `divideComandaOld` — línea 855.
- `agregaComanda` — línea 948.
- `generaArchivos` — línea 963.
- `getProd` — línea 1059.
- `bigtoast` — línea 1071.
- `ventaVacia` — línea 1086.
- `borrarVenta` — línea 1100.
- `iniciaTiempo` — línea 1123.
- `run` — línea 1126.
- `run` — línea 1128.
- `cancelaTiempo` — línea 1137.
- `actualizaTiempo` — línea 1143.
- `montoPago` — línea 1160.
- `splitByLen` — línea 1173.
- `pantallaHorizontal` — línea 1182.
- `addItemPedidoCom` — línea 1192.
- `esIngrediente` — línea 1205.
- `esIngrediente` — línea 1215.
- `msgAsk` — línea 1229.
- `onClick` — línea 1235.
- `onClick` — línea 1241.
- `msgAskAnul` — línea 1248.
- `onClick` — línea 1254.
- `onClick` — línea 1260.
- `msgAskAnul2` — línea 1267.
- `onClick` — línea 1273.
- `onClick` — línea 1279.
- `msgAskVenta` — línea 1286.
- `onClick` — línea 1292.
- `onClick` — línea 1298.
- `msgAskPago` — línea 1305.
- `onClick` — línea 1311.
- `onClick` — línea 1317.
- `msgAskFinish` — línea 1324.
- `onClick` — línea 1332.
- `onClick` — línea 1345.
- `msgAskReturn` — línea 1354.
- `onClick` — línea 1362.
- `onClick` — línea 1380.
- `msgConfirmExit` — línea 1389.
- `onClick` — línea 1397.
- `msgAskRePrint` — línea 1408.
- `onClick` — línea 1416.
- `onClick` — línea 1423.
- `msgAskReSend` — línea 1432.
- `onClick` — línea 1440.
- `onClick` — línea 1450.
- `onResume` — línea 1463.
- `onPause` — línea 1492.
- `onBackPressed` — línea 1498.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

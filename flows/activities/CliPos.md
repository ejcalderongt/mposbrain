# CliPos

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CliPos.java:49`; hereda `PBase`.

## Layouts candidatos

- `activity_cli_pos` — `app/src/main/java/com/dtsgt/mpos/CliPos.java:79`.
- `activity_cli_pos_port` — `app/src/main/java/com/dtsgt/mpos/CliPos.java:82`.
- `activity_cli_pos_ver` — `app/src/main/java/com/dtsgt/mpos/CliPos.java:84`.

## Navegación candidata

- `Clientes` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliPos.java:320`; condiciones en catálogo.
- `CliDirList` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliPos.java:357`; condiciones en catálogo.
- `Municipio` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliPos.java:366`; condiciones en catálogo.
- `ContrGrande` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliPos.java:1735`; condiciones en catálogo.

## Estado global escrito

`InvCompSend`, `cf_domicilio`, `cliente`, `cliente_credito`, `cliente_dom`, `codigo_cliente`, `contrib`, `dias_credito`, `dom_ddir`, `dom_dir`, `dom_nit`, `dom_nom`, `dom_ref`, `dom_tel`, `domicilio`, `gCorreoCliente`, `gDirCliente`, `gNITCliente`, `gNombreCliente`, `gTelCliente`, `gstr`, `limite_credito`, `media`, `mododocesa`, `nit_tipo`, `nivel`, `parallevar`, `pedcorel`, `percepcion`, `rutatipo`, `sal_NIT`, `sal_NRC`, `sal_PER`, `sal_idneg`, `scancliente`, `sel_nivel_prec`, `timeout`, `ventalock`, `wsurl`

## Tablas mencionadas estáticamente

`D_PEDIDO`, `D_PEDIDOCOMBO`, `D_PEDIDOD`, `P_CLIENTE`, `P_MUNICIPIO`, `T_PEDIDOD`, `T_VENTA`

## Métodos

- `onCreate` — línea 74.
- `consFinal` — línea 178.
- `clienteNIT` — línea 205.
- `buscarCliente` — línea 317.
- `doDomicilio` — línea 323.
- `doDireccion` — línea 335.
- `doMuni` — línea 365.
- `setHandlers` — línea 369.
- `onKey` — línea 373.
- `onFocusChange` — línea 385.
- `onCheckedChanged` — línea 392.
- `onCheckedChanged` — línea 404.
- `ingresaNIT` — línea 424.
- `procesaCF` — línea 439.
- `procesaNIT` — línea 492.
- `terminaCliente` — línea 551.
- `cargaCliente` — línea 601.
- `iniciaPedidos` — línea 622.
- `cancelaPedidos` — línea 644.
- `recibePedidos` — línea 650.
- `hidePanel` — línea 692.
- `run` — línea 694.
- `showPanel` — línea 702.
- `run` — línea 704.
- `crearPedido` — línea 716.
- `crearPedidoEncabezado` — línea 769.
- `addItemSqlNoImage` — línea 811.
- `crearPedidoDetalle` — línea 837.
- `agregaClientePedido` — línea 919.
- `menuPedidos` — línea 945.
- `validaNIT` — línea 965.
- `validaNITOld` — línea 1041.
- `buscarCliente` — línea 1116.
- `buscaCliente` — línea 1138.
- `existeCliente` — línea 1173.
- `agregaCliente` — línea 1242.
- `agregaClienteCF` — línea 1329.
- `actualizaCliente` — línea 1369.
- `purgeNIT` — línea 1404.
- `nitnum` — línea 1436.
- `nitnumhn` — línea 1466.
- `nitnumsv` — línea 1478.
- `limpiaCampos` — línea 1496.
- `getURL` — línea 1506.
- `hasProducts` — línea 1526.
- `esCF` — línea 1542.
- `clientePorNIT` — línea 1553.
- `pantallaPortrait` — línea 1567.
- `pantallaHorizontal` — línea 1577.
- `consultaNITInfile` — línea 1592.
- `onResponse` — línea 1620.
- `onErrorResponse` — línea 1636.
- `buscaRTN` — línea 1646.
- `buscaNCR` — línea 1671.
- `municipio` — línea 1696.
- `msgAskCG` — línea 1719.
- `onClick` — línea 1726.
- `onClick` — línea 1743.
- `msgAskOrden` — línea 1763.
- `onClick` — línea 1774.
- `onClick` — línea 1780.
- `msgExit` — línea 1787.
- `onClick` — línea 1794.
- `onResume` — línea 1806.
- `onPause` — línea 1862.
- `onBackPressed` — línea 1868.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

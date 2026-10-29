# CliPosPan

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CliPosPan.java:40`; hereda `PBase`.

## Layouts candidatos

- `activity_cli_pos_pan` — `app/src/main/java/com/dtsgt/mpos/CliPosPan.java:66`.

## Navegación candidata

- `Clientes` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliPosPan.java:212`; condiciones en catálogo.
- `CliDirList` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliPosPan.java:249`; condiciones en catálogo.
- `Municipio` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliPosPan.java:258`; condiciones en catálogo.

## Estado global escrito

`InvCompSend`, `cf_domicilio`, `cliente`, `cliente_credito`, `cliente_dom`, `codigo_cliente`, `contrib`, `dias_credito`, `dom_ddir`, `dom_dir`, `dom_nit`, `dom_nom`, `dom_ref`, `dom_tel`, `domicilio`, `gCorreoCliente`, `gDirCliente`, `gNITCliente`, `gNombreCliente`, `gTelCliente`, `gstr`, `limite_credito`, `media`, `mododocesa`, `nit_tipo`, `nivel`, `parallevar`, `pedcorel`, `percepcion`, `rutatipo`, `sal_NIT`, `sal_PER`, `scancliente`, `timeout`, `ventalock`, `wsurl`

## Tablas mencionadas estáticamente

`D_PEDIDO`, `D_PEDIDOCOMBO`, `D_PEDIDOD`, `P_CLIENTE`, `P_MUNICIPIO`, `T_PEDIDOD`, `T_VENTA`

## Métodos

- `onCreate` — línea 61.
- `consFinal` — línea 126.
- `clienteNIT` — línea 152.
- `buscarCliente` — línea 209.
- `doDomicilio` — línea 215.
- `doDireccion` — línea 227.
- `doMuni` — línea 257.
- `setHandlers` — línea 261.
- `onKey` — línea 265.
- `onFocusChange` — línea 277.
- `onCheckedChanged` — línea 284.
- `onCheckedChanged` — línea 296.
- `ingresaNIT` — línea 316.
- `procesaCF` — línea 324.
- `procesaNIT` — línea 374.
- `terminaCliente` — línea 416.
- `cargaCliente` — línea 452.
- `crearPedido` — línea 473.
- `crearPedidoEncabezado` — línea 526.
- `addItemSqlNoImage` — línea 568.
- `crearPedidoDetalle` — línea 594.
- `agregaClientePedido` — línea 676.
- `validaRUC` — línea 706.
- `tipoIdent` — línea 717.
- `buscarCliente` — línea 735.
- `existeCliente` — línea 757.
- `agregaCliente` — línea 819.
- `agregaClienteCF` — línea 897.
- `actualizaCliente` — línea 937.
- `purgeNIT` — línea 962.
- `rucnum` — línea 995.
- `limpiaCampos` — línea 1012.
- `getURL` — línea 1022.
- `hasProducts` — línea 1042.
- `esCF` — línea 1058.
- `clientePorNIT` — línea 1069.
- `pantallaHorizontal` — línea 1083.
- `municipio` — línea 1093.
- `msgExit` — línea 1116.
- `onClick` — línea 1123.
- `onResume` — línea 1135.
- `onPause` — línea 1172.
- `onBackPressed` — línea 1178.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

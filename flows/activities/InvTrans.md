# InvTrans

Dominio: `inventory`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/InvTrans.java:46`; hereda `PBase`.

## Layouts candidatos

- `activity_inv_trans` — `app/src/main/java/com/dtsgt/mpos/InvTrans.java:98`.
- `activity_inv_trans_ver` — `app/src/main/java/com/dtsgt/mpos/InvTrans.java:100`.

## Navegación candidata

- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvTrans.java:572`; condiciones en catálogo.

## Estado global escrito

`autocom`, `barra`, `codigo_proveedor`

## Tablas mencionadas estáticamente

`D_MOV`, `D_MOVD_ALMACEN`, `D_MOV_ALMACEN`, `P_PRODUCTO`, `P_STOCK`, `P_STOCK_ALMACEN`, `T_COSTO`, `T_MOVR`, `T_STOCK`

## Métodos

- `onCreate` — línea 90.
- `doAdd` — línea 177.
- `doSave` — línea 182.
- `doFocusBar` — línea 200.
- `doFocusCant` — línea 205.
- `doFocusCosto` — línea 209.
- `doKey` — línea 213.
- `doListUnits` — línea 235.
- `doHideList` — línea 239.
- `doProd` — línea 243.
- `doClearFilter` — línea 247.
- `setHandlers` — línea 252.
- `onItemClick` — línea 256.
- `onItemClick` — línea 270.
- `onItemClick` — línea 282.
- `onFocusChange` — línea 294.
- `afterTextChanged` — línea 308.
- `beforeTextChanged` — línea 310.
- `onTextChanged` — línea 312.
- `run` — línea 319.
- `listItems` — línea 336.
- `addItem` — línea 373.
- `savealmacen` — línea 470.
- `addBarcode` — línea 583.
- `barraProducto` — línea 595.
- `setProduct` — línea 656.
- `setProductr` — línea 684.
- `ingresoStock` — línea 712.
- `ingresoStockAlmacen` — línea 720.
- `egresoStock` — línea 728.
- `egresoStockAlmacen` — línea 737.
- `ingresoStockOld` — línea 746.
- `ingresoStockAlmacenOld` — línea 777.
- `egresoStockOld` — línea 826.
- `egresoStockAlmacenOld` — línea 831.
- `updateStock` — línea 837.
- `converUMBas` — línea 849.
- `cargaDatos` — línea 868.
- `cargaDatosAlmacen` — línea 917.
- `iniciaProceso` — línea 970.
- `processMenuBtn` — línea 1003.
- `borraLinea` — línea 1026.
- `borraTodo` — línea 1039.
- `fbListItems` — línea 1047.
- `prodnom` — línea 1073.
- `iniciaProductos` — línea 1084.
- `codigoProducto` — línea 1109.
- `buscarProducto` — línea 1155.
- `imprimir` — línea 1216.
- `impresionEncabezado` — línea 1241.
- `impresionDetalle` — línea 1261.
- `getFbProdStock` — línea 1284.
- `fbCallBack` — línea 1296.
- `creaEncabezadoInicial` — línea 1313.
- `borraEncabezadoInicial` — línea 1340.
- `nombreUnidad` — línea 1348.
- `listUnits` — línea 1362.
- `onItemClick` — línea 1374.
- `onClick` — línea 1384.
- `pantallaHorizontal` — línea 1397.
- `dispProdUni` — línea 1407.
- `dispProdUniOld` — línea 1416.
- `dispProd` — línea 1441.
- `compareSC` — línea 1458.
- `nombreAlmacen` — línea 1478.
- `msgAskTodo` — línea 1493.
- `onClick` — línea 1499.
- `onClick` — línea 1511.
- `msgAskSave` — línea 1518.
- `onClick` — línea 1524.
- `onClick` — línea 1534.
- `msgAskExit` — línea 1541.
- `onClick` — línea 1548.
- `onClick` — línea 1554.
- `msgAskCant` — línea 1561.
- `onClick` — línea 1567.
- `onClick` — línea 1574.
- `onResume` — línea 1585.
- `onBackPressed` — línea 1611.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

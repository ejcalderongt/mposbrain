# InvRecep

Dominio: `inventory`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/InvRecep.java:54`; hereda `PBase`.

## Layouts candidatos

- `activity_inv_recep` — `app/src/main/java/com/dtsgt/mpos/InvRecep.java:105`.

## Navegación candidata

- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvRecep.java:732`; condiciones en catálogo.
- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvRecep.java:854`; condiciones en catálogo.

## Estado global escrito

`autocom`, `barra`, `codigo_proveedor`, `nombre_proveedor`

## Tablas mencionadas estáticamente

`D_MOV`, `D_MOVD`, `D_MOVD_ALMACEN`, `D_MOV_ALMACEN`, `P_PRODUCTO`, `T_COSTO`, `T_MOVD`, `T_MOVR`, `T_STOCK`

## Métodos

- `onCreate` — línea 100.
- `run` — línea 174.
- `run` — línea 181.
- `doAdd` — línea 221.
- `doSave` — línea 225.
- `doFocusBar` — línea 254.
- `doFocusCant` — línea 260.
- `doFocusCosto` — línea 266.
- `doKey` — línea 272.
- `doListUnits` — línea 298.
- `doInterrupt` — línea 303.
- `doDoc` — línea 308.
- `doHideList` — línea 312.
- `doProd` — línea 316.
- `doClearFilter` — línea 320.
- `setHandlers` — línea 324.
- `onItemClick` — línea 346.
- `afterTextChanged` — línea 378.
- `beforeTextChanged` — línea 381.
- `onTextChanged` — línea 384.
- `listItems` — línea 406.
- `addItem` — línea 489.
- `save` — línea 604.
- `savealmacen` — línea 743.
- `addBarcode` — línea 865.
- `barraProducto` — línea 880.
- `setProduct` — línea 933.
- `setProductr` — línea 969.
- `updateStock` — línea 1002.
- `updateStockAlmacen` — línea 1019.
- `converUMBas` — línea 1040.
- `cargaDatos` — línea 1060.
- `actualizaExistencias` — línea 1120.
- `cargaDatosAlmacen` — línea 1139.
- `hold` — línea 1194.
- `holdalmacen` — línea 1280.
- `iniciaProceso` — línea 1375.
- `processMenuBtn` — línea 1417.
- `borraLinea` — línea 1445.
- `borraTodo` — línea 1459.
- `imprimir` — línea 1467.
- `impresionEncabezado` — línea 1494.
- `impresionDetalle` — línea 1523.
- `getFbProdStock` — línea 1547.
- `fbCallBack` — línea 1558.
- `fbListItems` — línea 1626.
- `iniciaProductos` — línea 1635.
- `codigoProducto` — línea 1663.
- `buscarProducto` — línea 1710.
- `nombreUnidad` — línea 1748.
- `listUnitsTallaColor` — línea 1777.
- `compare` — línea 1804.
- `updateStockAlmacenTallaColor` — línea 1839.
- `nombreColor` — línea 1861.
- `esTallaColor` — línea 1874.
- `creaEncabezadoInicial` — línea 1891.
- `borraEncabezadoInicial` — línea 1920.
- `nombreProveedor` — línea 1929.
- `listUnits` — línea 1939.
- `pantallaHorizontal` — línea 1973.
- `dispProdUni` — línea 1983.
- `dispProd` — línea 1992.
- `compareSC` — línea 2010.
- `msgAskTodo` — línea 2034.
- `msgAskSave` — línea 2052.
- `msgAskSave2` — línea 2067.
- `msgAskExit` — línea 2084.
- `msgAskInterrupt` — línea 2092.
- `inputDoc` — línea 2108.
- `onResume` — línea 2136.
- `onBackPressed` — línea 2170.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

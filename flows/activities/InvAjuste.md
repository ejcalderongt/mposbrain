# InvAjuste

Dominio: `inventory`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/InvAjuste.java:56`; hereda `PBase`.

## Layouts candidatos

- `activity_inv_salida` — `app/src/main/java/com/dtsgt/mpos/InvAjuste.java:112`.
- `activity_inv_salida_ver` — `app/src/main/java/com/dtsgt/mpos/InvAjuste.java:114`.

## Navegación candidata

- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvAjuste.java:528`; condiciones en catálogo.
- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvAjuste.java:606`; condiciones en catálogo.

## Estado global escrito

`autocom`, `barra`

## Tablas mencionadas estáticamente

`D_MOVD`, `D_MOVD_ALMACEN`, `P_PRODUCTO`, `P_STOCK`, `P_STOCK_ALMACEN`, `T_MOVD`, `T_MOVR`, `T_STOCK`

## Métodos

- `onCreate` — línea 108.
- `run` — línea 173.
- `run` — línea 180.
- `doSave` — línea 195.
- `doFocusBar` — línea 202.
- `doFocusCant` — línea 210.
- `doFocusCosto` — línea 214.
- `doKey` — línea 218.
- `doListUnits` — línea 235.
- `doDisp` — línea 239.
- `doHideList` — línea 251.
- `doProd` — línea 255.
- `doClearFilter` — línea 259.
- `doFecha` — línea 263.
- `setHandlers` — línea 267.
- `onItemClick` — línea 271.
- `onItemClick` — línea 284.
- `onItemClick` — línea 296.
- `afterTextChanged` — línea 309.
- `beforeTextChanged` — línea 311.
- `onTextChanged` — línea 313.
- `run` — línea 320.
- `listItems` — línea 337.
- `addItem` — línea 379.
- `save` — línea 456.
- `savealmacen` — línea 541.
- `addBarcode` — línea 616.
- `barraProducto` — línea 627.
- `setProduct` — línea 692.
- `adjustStock` — línea 723.
- `adjustStockAlmacen` — línea 739.
- `adjustStockAlmacenOld` — línea 760.
- `adjustStockOld` — línea 767.
- `iniciaProceso` — línea 844.
- `processMenuBtn` — línea 884.
- `borraLinea` — línea 910.
- `borraTodo` — línea 922.
- `iniciaProductos` — línea 930.
- `codigoProducto` — línea 958.
- `buscarProducto` — línea 1007.
- `imprimir` — línea 1051.
- `impresionEncabezado` — línea 1077.
- `impresionDetalle` — línea 1102.
- `nombreUnidad` — línea 1125.
- `listUnitsTallaColor` — línea 1156.
- `compare` — línea 1183.
- `updateStockAlmacenTallaColor` — línea 1218.
- `nombreColor` — línea 1240.
- `esTallaColor` — línea 1253.
- `runFbCallBack` — línea 1271.
- `getFbProdStock` — línea 1283.
- `fbListItems` — línea 1348.
- `nombreMotivo` — línea 1357.
- `pantallaHorizontal` — línea 1366.
- `dispProdUni` — línea 1376.
- `dispProd` — línea 1385.
- `compareSC` — línea 1405.
- `cambiaFecha` — línea 1425.
- `onDateSet` — línea 1429.
- `listUnits` — línea 1444.
- `listaMotivos` — línea 1485.
- `onItemClick` — línea 1500.
- `onClick` — línea 1513.
- `msgAskTodo` — línea 1527.
- `onClick` — línea 1533.
- `onClick` — línea 1545.
- `msgAskSave` — línea 1552.
- `onClick` — línea 1558.
- `onClick` — línea 1568.
- `msgAskSave2` — línea 1575.
- `onClick` — línea 1581.
- `onClick` — línea 1595.
- `msgAskExit` — línea 1602.
- `onClick` — línea 1608.
- `onClick` — línea 1614.
- `onResume` — línea 1625.
- `onBackPressed` — línea 1655.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

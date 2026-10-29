# InvEgreso

Dominio: `inventory`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/InvEgreso.java:39`; hereda `PBase`.

## Layouts candidatos

- `activity_inv_egreso` — `app/src/main/java/com/dtsgt/mpos/InvEgreso.java:76`.
- `activity_inv_egreso_ver` — `app/src/main/java/com/dtsgt/mpos/InvEgreso.java:78`.

## Navegación candidata

- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvEgreso.java:437`; condiciones en catálogo.
- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvEgreso.java:516`; condiciones en catálogo.
- `Producto` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvEgreso.java:713`; condiciones en catálogo.

## Estado global escrito

`autocom`, `barra`, `gstr`, `idalm`, `idalmpred`, `prodtipo`

## Tablas mencionadas estáticamente

`D_MOVD`, `D_MOVD_ALMACEN`, `P_PRODUCTO`, `P_STOCK`, `P_STOCK_ALMACEN`, `T_MOVD`, `T_MOVR`

## Métodos

- `onCreate` — línea 70.
- `doSave` — línea 137.
- `doFocusBar` — línea 144.
- `doFocusCant` — línea 152.
- `doFocusCosto` — línea 156.
- `doKey` — línea 160.
- `setHandlers` — línea 178.
- `onItemClick` — línea 182.
- `onItemClick` — línea 195.
- `afterTextChanged` — línea 208.
- `beforeTextChanged` — línea 210.
- `onTextChanged` — línea 212.
- `run` — línea 219.
- `listItems` — línea 236.
- `addItem` — línea 277.
- `save` — línea 372.
- `savealmacen` — línea 447.
- `addBarcode` — línea 526.
- `barraProducto` — línea 537.
- `setProduct` — línea 599.
- `adjustStock` — línea 628.
- `adjustStockAlmacen` — línea 636.
- `updateStock` — línea 644.
- `iniciaProceso` — línea 665.
- `processMenuBtn` — línea 702.
- `borraLinea` — línea 727.
- `borraTodo` — línea 739.
- `imprimir` — línea 747.
- `impresionEncabezado` — línea 773.
- `impresionDetalle` — línea 792.
- `nombreMotivo` — línea 815.
- `pantallaHorizontal` — línea 824.
- `dispProdUni` — línea 834.
- `dispProd` — línea 859.
- `compareSC` — línea 876.
- `listaMotivos` — línea 900.
- `onItemClick` — línea 915.
- `onClick` — línea 930.
- `msgAskTodo` — línea 944.
- `onClick` — línea 950.
- `onClick` — línea 962.
- `msgAskSave` — línea 969.
- `onClick` — línea 975.
- `onClick` — línea 985.
- `msgAskSave2` — línea 992.
- `onClick` — línea 998.
- `onClick` — línea 1012.
- `msgAskExit` — línea 1019.
- `onClick` — línea 1025.
- `onClick` — línea 1031.
- `msgAskCant` — línea 1038.
- `onClick` — línea 1044.
- `onClick` — línea 1051.
- `onResume` — línea 1063.
- `onBackPressed` — línea 1086.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

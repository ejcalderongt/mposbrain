# ProdMenu

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/ProdMenu.java:30`; hereda `PBase`.

## Layouts candidatos

- `activity_prod_menu` — `app/src/main/java/com/dtsgt/mpos/ProdMenu.java:58`.

## Navegación candidata

- `Producto` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ProdMenu.java:156`; condiciones en catálogo.

## Estado global escrito

`gstr`, `prodtipo`, `retcant`

## Tablas mencionadas estáticamente

`P_IMPUESTO`, `P_PRODPRECIO`, `P_PRODUCTO`, `P_STOCK`, `T_COMBO`, `T_ORDEN`, `T_ORDENCOMBO`, `T_ORDENCOMBOAD`, `T_ORDENCOMBODET`, `T_ORDENCOMBOPRECIO`, `T_VENTA`

## Métodos

- `onCreate` — línea 53.
- `doApply` — línea 124.
- `doDec` — línea 137.
- `doInc` — línea 143.
- `doDelete` — línea 149.
- `doAdd` — línea 153.
- `doClose` — línea 159.
- `setHandlers` — línea 163.
- `onItemClick` — línea 168.
- `listItems` — línea 198.
- `updateItems` — línea 249.
- `newItem` — línea 285.
- `listMenuItems` — línea 290.
- `llenaPredeterminado` — línea 359.
- `listOptions` — línea 385.
- `onItemClick` — línea 423.
- `onClick` — línea 457.
- `saveItem` — línea 554.
- `deleteItem` — línea 661.
- `agregaArticulo` — línea 688.
- `precioFinal` — línea 779.
- `precioInicial` — línea 819.
- `precioItem` — línea 834.
- `guardaPrecios` — línea 856.
- `validaStock` — línea 873.
- `stockProducto` — línea 896.
- `cantStock` — línea 915.
- `cantProdVenta` — línea 940.
- `cantProdCombo` — línea 959.
- `cantProdItems` — línea 975.
- `isProdStock` — línea 990.
- `validaData` — línea 1005.
- `exit` — línea 1014.
- `prodPrecioBaseImp` — línea 1027.
- `getProdName` — línea 1099.
- `getProdUM` — línea 1108.
- `prodPrecioItem` — línea 1117.
- `msgAskDelete` — línea 1133.
- `onClick` — línea 1141.
- `onClick` — línea 1147.
- `msgAskExit` — línea 1156.
- `onClick` — línea 1165.
- `onClick` — línea 1172.
- `msgAskApply` — línea 1181.
- `onClick` — línea 1187.
- `onClick` — línea 1193.
- `msgAskSave` — línea 1200.
- `onClick` — línea 1206.
- `onClick` — línea 1212.
- `listaInvalidos` — línea 1219.
- `onClick` — línea 1231.
- `mostrarLista` — línea 1242.
- `onItemClick` — línea 1252.
- `onClick` — línea 1262.
- `onResume` — línea 1279.
- `onBackPressed` — línea 1297.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

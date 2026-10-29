# OrdenMenu

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/OrdenMenu.java:34`; hereda `PBase`.

## Layouts candidatos

- `activity_orden_menu` — `app/src/main/java/com/dtsgt/mpos/OrdenMenu.java:72`.

## Navegación candidata

- `Producto` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/OrdenMenu.java:190`; condiciones en catálogo.

## Estado global escrito

`dval`, `gstr`, `menuitemid`, `prodtipo`, `retcant`, `um`

## Tablas mencionadas estáticamente

`P_IMPUESTO`, `P_PRODPRECIO`, `P_PRODUCTO`, `T_ORDENCOMBOAD`, `T_ORDENCOMBODET`

## Métodos

- `onCreate` — línea 66.
- `doApply` — línea 162.
- `doDec` — línea 173.
- `doInc` — línea 178.
- `doDelete` — línea 183.
- `doAdd` — línea 187.
- `doClose` — línea 193.
- `setHandlers` — línea 197.
- `onItemClick` — línea 202.
- `listItems` — línea 231.
- `fbocaList` — línea 239.
- `fbocdList` — línea 257.
- `fbocbList` — línea 276.
- `updateItems` — línea 343.
- `newItem` — línea 379.
- `listMenuItems` — línea 393.
- `saveItem` — línea 461.
- `listOptions` — línea 573.
- `onItemClick` — línea 613.
- `onClick` — línea 644.
- `deleteItem` — línea 657.
- `agregaArticulo` — línea 687.
- `precioFinal` — línea 795.
- `precioInicial` — línea 830.
- `precioItem` — línea 845.
- `guardaPrecios` — línea 867.
- `validaData` — línea 884.
- `exit` — línea 893.
- `getProdName` — línea 906.
- `getProdUM` — línea 915.
- `prodPrecioItem` — línea 924.
- `prodPrecioBaseImp` — línea 936.
- `msgAskDelete` — línea 1014.
- `onClick` — línea 1021.
- `onClick` — línea 1027.
- `msgAskExit` — línea 1036.
- `onClick` — línea 1044.
- `onClick` — línea 1051.
- `msgAskApply` — línea 1060.
- `onClick` — línea 1065.
- `onClick` — línea 1071.
- `msgAskSave` — línea 1078.
- `onClick` — línea 1083.
- `onClick` — línea 1089.
- `listaInvalidos` — línea 1096.
- `onClick` — línea 1108.
- `mostrarLista` — línea 1119.
- `onItemClick` — línea 1130.
- `onClick` — línea 1139.
- `onResume` — línea 1156.
- `onBackPressed` — línea 1175.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

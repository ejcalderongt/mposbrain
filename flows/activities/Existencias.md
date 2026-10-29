# Existencias

Dominio: `inventory`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/Existencias.java:37`; hereda `PBase`.

## Layouts candidatos

- `activity_existencias` — `app/src/main/java/com/dtsgt/mpos/Existencias.java:76`.

## Navegación candidata


## Estado global escrito

`idalm`, `idalmpred`, `nom_alm`, `validimp`

## Tablas mencionadas estáticamente

`P_PRODUCTO`, `P_STOCK`, `T_STOCK`

## Métodos

- `onCreate` — línea 72.
- `doAlmacenes` — línea 139.
- `printDoc` — línea 143.
- `doRefresh` — línea 157.
- `doSearch` — línea 161.
- `doClean` — línea 185.
- `setHandlers` — línea 192.
- `onItemClick` — línea 197.
- `onItemLongClick` — línea 215.
- `afterTextChanged` — línea 234.
- `beforeTextChanged` — línea 256.
- `onTextChanged` — línea 258.
- `compareSC` — línea 279.
- `run` — línea 294.
- `listItems` — línea 307.
- `buildItemList` — línea 324.
- `validaFiltros` — línea 463.
- `showTallaColorMenu` — línea 488.
- `showTallaColorMenuOrig` — línea 549.
- `imprimirInventario` — línea 591.
- `CantExistencias` — línea 777.
- `tieneAlmacenes` — línea 803.
- `listaAlmacenes` — línea 827.
- `onItemClick` — línea 839.
- `onClick` — línea 861.
- `setDatosVersion` — línea 873.
- `cargaProductos` — línea 891.
- `msgAskImprimir` — línea 915.
- `onClick` — línea 921.
- `onClick` — línea 927.
- `msgboxexit` — línea 934.
- `onClick` — línea 941.
- `onResume` — línea 955.
- `onPause` — línea 966.
- `onBackPressed` — línea 976.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

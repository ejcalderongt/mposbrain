# InvAnular

Dominio: `inventory`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/InvAnular.java:51`; hereda `PBase`.

## Layouts candidatos

- `activity_inv_anular` — `app/src/main/java/com/dtsgt/mpos/InvAnular.java:83`.

## Navegación candidata

- `InicioInventario` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvAnular.java:326`; condiciones en catálogo.
- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvAnular.java:331`; condiciones en catálogo.
- `InicioInventario` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvAnular.java:413`; condiciones en catálogo.
- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvAnular.java:418`; condiciones en catálogo.

## Estado global escrito

`autocom`, `codigo_proveedor`, `idalm`, `idalmpred`, `nom_alm`

## Tablas mencionadas estáticamente

`D_MOVD`, `D_MOVD_ALMACEN`, `P_STOCK`, `T_MOVR`, `T_STOCK`

## Métodos

- `onCreate` — línea 79.
- `run` — línea 116.
- `doAlmacenes` — línea 148.
- `doAnul` — línea 152.
- `setHandlers` — línea 167.
- `onItemClick` — línea 172.
- `onItemLongClick` — línea 198.
- `afterTextChanged` — línea 216.
- `beforeTextChanged` — línea 218.
- `onTextChanged` — línea 220.
- `anulaInventario` — línea 238.
- `save` — línea 255.
- `savealmacen` — línea 348.
- `adjustStock` — línea 430.
- `adjustStockAlmacen` — línea 446.
- `listItems` — línea 466.
- `buildItemList` — línea 478.
- `tieneAlmacenes` — línea 642.
- `listaAlmacenes` — línea 667.
- `onItemClick` — línea 681.
- `onClick` — línea 699.
- `CreateFbCheckStatus` — línea 718.
- `onDataChange` — línea 721.
- `onCancelled` — línea 728.
- `onDataChange` — línea 742.
- `onCancelled` — línea 753.
- `msgAskAnul` — línea 776.
- `onClick` — línea 782.
- `onClick` — línea 788.
- `msgAskAnul2` — línea 795.
- `onClick` — línea 801.
- `onClick` — línea 807.
- `msgboxexit` — línea 814.
- `onClick` — línea 821.
- `onResume` — línea 834.
- `onPause` — línea 847.
- `onBackPressed` — línea 860.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

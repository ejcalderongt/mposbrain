# ProdMenuCant

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/ProdMenuCant.java:22`; hereda `PBase`.

## Layouts candidatos

- `activity_prod_menu_cant` — `app/src/main/java/com/dtsgt/mpos/ProdMenuCant.java:45`.

## Navegación candidata

- `CantKeyb` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ProdMenuCant.java:110`; condiciones en catálogo.

## Estado global escrito

`retcant`, `set_cant_max`

## Tablas mencionadas estáticamente

`P_PRODMENUOPC_DET`, `P_PRODUCTO`, `T_COMBO`, `T_ORDENCOMBOPRECIO`, `T_VENTA`

## Métodos

- `onCreate` — línea 41.
- `doApply` — línea 78.
- `doDelete` — línea 89.
- `doClose` — línea 93.
- `setHandlers` — línea 97.
- `onItemClick` — línea 100.
- `listItems` — línea 119.
- `newItem` — línea 129.
- `loadItems` — línea 137.
- `listOptions` — línea 155.
- `updateCant` — línea 196.
- `saveItem` — línea 208.
- `guardaPrecios` — línea 297.
- `calcTotal` — línea 314.
- `msgAskSave` — línea 327.
- `onClick` — línea 333.
- `onClick` — línea 339.
- `msgAskExit` — línea 345.
- `onClick` — línea 354.
- `onClick` — línea 361.
- `onResume` — línea 374.
- `onBackPressed` — línea 392.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

# BonList

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/BonList.java:31`; hereda `PBase`.

## Layouts candidatos

- `activity_bon_list` — `app/src/main/java/com/dtsgt/mpos/BonList.java:55`.

## Navegación candidata

- `Producto` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/BonList.java:111`; condiciones en catálogo.

## Estado global escrito

`gstr`, `prodtipo`

## Tablas mencionadas estáticamente

`P_PRODUCTO`, `P_STOCK`, `T_BONIFFALT`, `T_BONITEM`

## Métodos

- `onCreate` — línea 52.
- `nextScreen` — línea 95.
- `selectProd` — línea 104.
- `sethandlers` — línea 119.
- `onItemClick` — línea 123.
- `showBonList` — línea 155.
- `listItems` — línea 193.
- `applyBon` — línea 258.
- `addItem` — línea 290.
- `addFalt` — línea 334.
- `showStat` — línea 351.
- `processNextScreen` — línea 395.
- `processItem` — línea 413.
- `setVarCant` — línea 457.
- `onClick` — línea 498.
- `onClick` — línea 522.
- `setVarAllCant` — línea 537.
- `onClick` — línea 574.
- `onClick` — línea 601.
- `onClick` — línea 605.
- `inputCant` — línea 628.
- `setItem` — línea 640.
- `nextItem` — línea 670.
- `msgAskDel` — línea 688.
- `onClick` — línea 695.
- `onClick` — línea 708.
- `getDisp` — línea 720.
- `getMargin` — línea 746.
- `toastcnt` — línea 760.
- `clearByProd` — línea 774.
- `showkeyb` — línea 794.
- `prodPorPeso` — línea 802.
- `onResume` — línea 814.
- `onBackPressed` — línea 830.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

# SolicInv

Dominio: `inventory`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/SolicInv.java:22`; hereda `PBase`.

## Layouts candidatos

- `activity_solic_inv` — `app/src/main/java/com/dtsgt/mpos/SolicInv.java:39`.

## Navegación candidata

- `Producto` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/SolicInv.java:62`; condiciones en catálogo.
- `RecargCant` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/SolicInv.java:224`; condiciones en catálogo.
- `RecargCant` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/SolicInv.java:237`; condiciones en catálogo.

## Estado global escrito

No detectado.

## Tablas mencionadas estáticamente

`D_SOLICINV`, `D_SOLICINVD`, `P_PRODUCTO`

## Métodos

- `onCreate` — línea 36.
- `showProd` — línea 57.
- `finishDevol` — línea 70.
- `doExit` — línea 83.
- `doClear` — línea 92.
- `setHandlers` — línea 104.
- `onItemClick` — línea 107.
- `onItemLongClick` — línea 127.
- `listItems` — línea 150.
- `processItem` — línea 201.
- `setCant` — línea 217.
- `updCant` — línea 232.
- `processCant` — línea 244.
- `addItem` — línea 267.
- `saveDevol` — línea 306.
- `clearData` — línea 323.
- `msgAskClear` — línea 335.
- `onClick` — línea 346.
- `onClick` — línea 352.
- `msgAskComplete` — línea 365.
- `onClick` — línea 375.
- `onClick` — línea 381.
- `msgAskDelete` — línea 394.
- `onClick` — línea 404.
- `onClick` — línea 419.
- `hasProducts` — línea 432.
- `getCorel` — línea 446.
- `onResume` — línea 464.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

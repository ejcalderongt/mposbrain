# ProdCant

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/ProdCant.java:28`; hereda `PBase`.

## Layouts candidatos

- `activity_prod_cant` — `app/src/main/java/com/dtsgt/mpos/ProdCant.java:45`.

## Navegación candidata

- `ListaPromo` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ProdCant.java:94`; condiciones en catálogo.
- `PicView` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ProdCant.java:107`; condiciones en catálogo.
- `ComWSExist` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ProdCant.java:132`; condiciones en catálogo.
- `ActDisp` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ProdCant.java:565`; condiciones en catálogo.

## Estado global escrito

`dpeso`, `dval`, `gstr`, `imgpath`, `prectemp`, `ubas`, `um`, `umfactor`, `umpres`, `umstock`

## Tablas mencionadas estáticamente

`P_FACTORCONV`, `P_NIVELPRECIO`, `P_PRODPRECIO`, `P_PRODUCTO`, `P_STOCK`, `T_BONITEM`, `T_VENTA`

## Métodos

- `onCreate` — línea 42.
- `sendCant` — línea 82.
- `showPromo` — línea 90.
- `showPic` — línea 102.
- `doDelete` — línea 114.
- `askExist` — línea 123.
- `onClick` — línea 130.
- `setHandlers` — línea 146.
- `afterTextChanged` — línea 151.
- `beforeTextChanged` — línea 154.
- `onTextChanged` — línea 157.
- `onKey` — línea 164.
- `afterTextChanged` — línea 182.
- `beforeTextChanged` — línea 184.
- `onTextChanged` — línea 186.
- `onKey` — línea 192.
- `showData` — línea 213.
- `getDisp` — línea 362.
- `delItem` — línea 487.
- `applyCant` — línea 499.
- `updDisp` — línea 559.
- `setControls` — línea 577.
- `setCant` — línea 604.
- `checkLimits` — línea 717.
- `setPrecio` — línea 721.
- `parseCant` — línea 761.
- `getDispInv` — línea 775.
- `paramProd` — línea 779.
- `forceClose` — línea 799.
- `msgSinPrecio` — línea 807.
- `onClick` — línea 813.
- `msgAskUpd` — línea 825.
- `onClick` — línea 834.
- `onClick` — línea 840.
- `msgAskDel` — línea 851.
- `onClick` — línea 858.
- `onClick` — línea 864.
- `msgAskAjust` — línea 873.
- `onClick` — línea 880.
- `onClick` — línea 886.
- `msgFactor` — línea 897.
- `onClick` — línea 903.
- `onResume` — línea 920.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

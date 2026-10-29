# FELContAnul

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/fel/FELContAnul.java:31`; hereda `PBase`.

## Layouts candidatos

- `activity_f_e_l_cont_anul` — `app/src/main/java/com/dtsgt/fel/FELContAnul.java:59`.

## Navegación candidata

- `FELFactura` (intent_candidate) — `app/src/main/java/com/dtsgt/fel/FELContAnul.java:120`; condiciones en catálogo.
- `FELFactura` (intent_candidate) — `app/src/main/java/com/dtsgt/fel/FELContAnul.java:198`; condiciones en catálogo.

## Estado global escrito

`felcorel`, `feluuid`, `timeout`, `wsurl`

## Tablas mencionadas estáticamente

`P_CLIENTE`

## Métodos

- `onCreate` — línea 56.
- `procesafactura` — línea 134.
- `run` — línea 140.
- `contingenciaFactura` — línea 148.
- `contingencia` — línea 155.
- `felCallBack` — línea 162.
- `callBackMulti` — línea 190.
- `buildAnulXML` — línea 203.
- `Get_NIT_Cliente` — línea 232.
- `buildList` — línea 262.
- `updateLabel` — línea 287.
- `run` — línea 290.
- `run` — línea 292.
- `prodName` — línea 301.
- `getURL` — línea 310.
- `msgexit` — línea 345.
- `showMsgExit` — línea 353.
- `onClick` — línea 360.
- `onResume` — línea 374.
- `onBackPressed` — línea 388.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

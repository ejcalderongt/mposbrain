# FELVerificacion

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/fel/FELVerificacion.java:43`; hereda `PBase`.

## Layouts candidatos

- `activity_fel_verificacion` — `app/src/main/java/com/dtsgt/fel/FELVerificacion.java:76`.

## Navegación candidata

- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/fel/FELVerificacion.java:284`; condiciones en catálogo.

## Estado global escrito

`autocom`, `feluuid`, `timeout`, `wsurl`

## Tablas mencionadas estáticamente

`D_FACTURA`

## Métodos

- `onCreate` — línea 72.
- `procesafactura` — línea 181.
- `contingenciaFactura` — línea 202.
- `contingencia` — línea 213.
- `felCallBack` — línea 231.
- `felProgress` — línea 267.
- `callBackMulti` — línea 274.
- `buildFactXML` — línea 289.
- `guardarXMLComoArchivo` — línea 465.
- `marcaFacturaContingencia` — línea 482.
- `procesaValidacion` — línea 540.
- `actualizaValidadas` — línea 552.
- `buildList` — línea 598.
- `updateLabel` — línea 631.
- `prodName` — línea 639.
- `getURL` — línea 649.
- `listaCombo` — línea 680.
- `msgexit` — línea 706.
- `showMsgExit` — línea 713.
- `msgexit3` — línea 730.
- `showMsgExit2` — línea 754.
- `onResume` — línea 772.
- `onBackPressed` — línea 788.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

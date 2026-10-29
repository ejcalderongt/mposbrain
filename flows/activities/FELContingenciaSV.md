# FELContingenciaSV

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/felesa/FELContingenciaSV.java:55`; hereda `PBase`.

## Layouts candidatos

- `activity_felcontingencia_sv` — `app/src/main/java/com/dtsgt/felesa/FELContingenciaSV.java:104`.

## Navegación candidata

- `FELmsgbox` (intent_candidate) — `app/src/main/java/com/dtsgt/felesa/FELContingenciaSV.java:222`; condiciones en catálogo.
- `FELmsgbox` (intent_candidate) — `app/src/main/java/com/dtsgt/felesa/FELContingenciaSV.java:409`; condiciones en catálogo.
- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/felesa/FELContingenciaSV.java:825`; condiciones en catálogo.

## Estado global escrito

`FELmsg`, `autocom`, `feluuid`, `timeout`, `wsurl`

## Tablas mencionadas estáticamente

`D_FACTURA_FEL_PAIS`

## Métodos

- `onCreate` — línea 99.
- `doHalt` — línea 202.
- `procesaDocumento` — línea 216.
- `certificaDocumento` — línea 234.
- `JSONfactura` — línea 263.
- `JSONcredito` — línea 310.
- `felCallBack` — línea 370.
- `callBackMulti` — línea 390.
- `marcaFactura` — línea 417.
- `guardaRespuestaFEL` — línea 439.
- `guardaError` — línea 496.
- `enviaErrores` — línea 525.
- `enviaError` — línea 539.
- `buildList` — línea 613.
- `updateLabel` — línea 636.
- `felProgress` — línea 644.
- `felDocument` — línea 653.
- `creaBitacora` — línea 661.
- `prodName` — línea 684.
- `getURL` — línea 693.
- `addUpdateItem` — línea 721.
- `maxconting` — línea 744.
- `listaCombo` — línea 755.
- `closeForm` — línea 774.
- `msgexit` — línea 787.
- `run` — línea 791.
- `showMsgExit` — línea 800.
- `showMsgExitEnvio` — línea 814.
- `onResume` — línea 840.
- `onBackPressed` — línea 859.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

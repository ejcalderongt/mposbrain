# FELFactura

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/fel/FELFactura.java:55`; hereda `PBase`.

## Layouts candidatos

- `activity_fel_factura` — `app/src/main/java/com/dtsgt/fel/FELFactura.java:106`.

## Navegación candidata

- `FELmsgbox` (intent_candidate) — `app/src/main/java/com/dtsgt/fel/FELFactura.java:515`; condiciones en catálogo.
- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/fel/FELFactura.java:1147`; condiciones en catálogo.

## Estado global escrito

`FELmsg`, `autocom`, `feluuid`, `timeout`, `wsurl`

## Tablas mencionadas estáticamente

`D_CXC`, `D_FACTURA`, `D_FACTURAC`, `D_FACTURAD`, `D_FACTURAD_TC`, `D_FACTURAP`, `D_FACTURAPR`, `D_FEL_ERROR`, `P_CLIENTE`, `P_COREL`

## Métodos

- `onCreate` — línea 100.
- `doHalt` — línea 217.
- `procesafactura` — línea 231.
- `certificaFactura` — línea 245.
- `procesaFirma` — línea 256.
- `multipleFacturas` — línea 301.
- `felCallBack` — línea 313.
- `felProgress` — línea 462.
- `callBackMulti` — línea 469.
- `callBackSingle` — línea 490.
- `registroFirebase` — línea 526.
- `buildFactXML` — línea 547.
- `guardarXMLComoArchivo` — línea 716.
- `marcaFactura` — línea 733.
- `marcaFacturaContingencia` — línea 756.
- `envioFactura` — línea 809.
- `processFactura` — línea 821.
- `addFactheader` — línea 942.
- `addPropinaItem` — línea 994.
- `D_factCaddItemSql` — línea 1012.
- `D_factRaddItemSql` — línea 1028.
- `D_fact_dTCaddItemSql` — línea 1040.
- `addCxCItemSql` — línea 1056.
- `statusFactura` — línea 1080.
- `processComplete` — línea 1108.
- `envioFacturas` — línea 1125.
- `envioMultiFactura` — línea 1140.
- `processMultiFactura` — línea 1153.
- `prepareSend` — línea 1213.
- `wsCallBack` — línea 1263.
- `buildList` — línea 1300.
- `updateLabel` — línea 1337.
- `updateLabelSend` — línea 1345.
- `prodName` — línea 1353.
- `getURL` — línea 1363.
- `guardaError` — línea 1394.
- `addUpdateItem` — línea 1420.
- `maxconting` — línea 1443.
- `listaCombo` — línea 1454.
- `closeForm` — línea 1473.
- `msgexit` — línea 1486.
- `run` — línea 1490.
- `showMsgExit` — línea 1499.
- `onResume` — línea 1516.
- `onBackPressed` — línea 1534.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

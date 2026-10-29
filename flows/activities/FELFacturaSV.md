# FELFacturaSV

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/felesa/FELFacturaSV.java:57`; hereda `PBase`.

## Layouts candidatos

- `activity_felfactura_sv` — `app/src/main/java/com/dtsgt/felesa/FELFacturaSV.java:112`.

## Navegación candidata

- `FELmsgbox` (intent_candidate) — `app/src/main/java/com/dtsgt/felesa/FELFacturaSV.java:423`; condiciones en catálogo.
- `FELmsgbox` (intent_candidate) — `app/src/main/java/com/dtsgt/felesa/FELFacturaSV.java:452`; condiciones en catálogo.
- `FELmsgbox` (intent_candidate) — `app/src/main/java/com/dtsgt/felesa/FELFacturaSV.java:635`; condiciones en catálogo.
- `FELmsgbox` (intent_candidate) — `app/src/main/java/com/dtsgt/felesa/FELFacturaSV.java:671`; condiciones en catálogo.
- `FELmsgbox` (intent_candidate) — `app/src/main/java/com/dtsgt/felesa/FELFacturaSV.java:691`; condiciones en catálogo.

## Estado global escrito

`FEL_llave_cont`, `FELmsg`, `feluuid`, `timeout`, `wsurl`

## Tablas mencionadas estáticamente

`D_FACTURA`, `D_FACTURAC`, `D_FACTURAD`, `D_FACTURAP`, `D_FACTURAPR`, `D_FACTURA_FEL_PAIS`, `D_FACTURA_SV`, `P_CLIENTE`, `P_COREL`

## Métodos

- `onCreate` — línea 107.
- `doHalt` — línea 222.
- `procesaDocumento` — línea 236.
- `certificaDocumento` — línea 255.
- `JSONfactura` — línea 284.
- `JSONcredito` — línea 328.
- `felCallBack` — línea 382.
- `callBackSingle` — línea 432.
- `marcaFactura` — línea 461.
- `guardaRespuestaFEL` — línea 482.
- `marcaFacturaContingencia` — línea 539.
- `generaLlaveContingencia` — línea 560.
- `contingenciaFactura` — línea 572.
- `contingenciaCF` — línea 584.
- `contFactura` — línea 606.
- `contCF` — línea 642.
- `guardaLlaveContingencia` — línea 679.
- `envioFactura` — línea 703.
- `processFactura` — línea 714.
- `addFactheader` — línea 829.
- `addPropinaItem` — línea 881.
- `D_factCaddItemSql` — línea 899.
- `D_factRaddItemSql` — línea 915.
- `D_factSVItemSql` — línea 927.
- `D_fact_fel_paisItemSql` — línea 940.
- `statusFactura` — línea 980.
- `processComplete` — línea 1002.
- `guardaError` — línea 1019.
- `writeToFile` — línea 1055.
- `enviaError` — línea 1075.
- `wsCallBack` — línea 1161.
- `updateLabel` — línea 1182.
- `felProgress` — línea 1190.
- `creaBitacora` — línea 1197.
- `prodName` — línea 1220.
- `getURL` — línea 1229.
- `addUpdateItem` — línea 1257.
- `maxconting` — línea 1280.
- `listaCombo` — línea 1291.
- `closeForm` — línea 1310.
- `msgexit` — línea 1323.
- `run` — línea 1327.
- `showMsgExit` — línea 1336.
- `onResume` — línea 1354.
- `onBackPressed` — línea 1372.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

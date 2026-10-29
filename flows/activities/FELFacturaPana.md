# FELFacturaPana

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/felpana/FELFacturaPana.java:47`; hereda `PBase`.

## Layouts candidatos

- `activity_felfactura_pana` — `app/src/main/java/com/dtsgt/felpana/FELFacturaPana.java:95`.

## Navegación candidata

- `FELmsgbox` (intent_candidate) — `app/src/main/java/com/dtsgt/felpana/FELFacturaPana.java:360`; condiciones en catálogo.
- `FELmsgbox` (intent_candidate) — `app/src/main/java/com/dtsgt/felpana/FELFacturaPana.java:375`; condiciones en catálogo.

## Estado global escrito

`FELmsg`, `feluuid`, `timeout`, `wsurl`

## Tablas mencionadas estáticamente

`D_FACTURA`, `D_FACTURAC`, `D_FACTURAD`, `D_FACTURAP`, `D_FACTURAPR`, `D_FACTURA_FEL_PAIS`, `D_FACTURA_SV`, `P_CLIENTE`, `P_COREL`

## Métodos

- `onCreate` — línea 91.
- `doHalt` — línea 168.
- `procesaFacturas` — línea 182.
- `inicializaFEL` — línea 207.
- `procesaDocumento` — línea 220.
- `certificaDocumento` — línea 246.
- `generaJson` — línea 257.
- `felCallBack` — línea 309.
- `callBackSingle` — línea 329.
- `terminaConError` — línea 352.
- `terminaConErrorSend` — línea 371.
- `marcaFactura` — línea 385.
- `guardaRespuestaFEL` — línea 407.
- `marcaFacturaContingencia` — línea 458.
- `envioFactura` — línea 476.
- `procesaFactura` — línea 487.
- `addFactheader` — línea 599.
- `addPropinaItem` — línea 652.
- `D_factCaddItemSql` — línea 670.
- `D_factRaddItemSql` — línea 686.
- `D_factSVItemSql` — línea 698.
- `D_fact_fel_paisItemSql` — línea 711.
- `statusFactura` — línea 751.
- `processComplete` — línea 775.
- `wsCallBack` — línea 807.
- `updateLabel` — línea 828.
- `felProgress` — línea 836.
- `creaBitacora` — línea 843.
- `prodName` — línea 866.
- `getURL` — línea 875.
- `addUpdateItem` — línea 903.
- `calcularDV` — línea 926.
- `maxconting` — línea 961.
- `listaCombo` — línea 972.
- `closeForm` — línea 991.
- `msgexit` — línea 1003.
- `run` — línea 1007.
- `showMsgExit` — línea 1016.
- `onResume` — línea 1034.
- `onBackPressed` — línea 1052.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

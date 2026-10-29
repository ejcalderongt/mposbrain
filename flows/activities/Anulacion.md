# Anulacion

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/Anulacion.java:72`; hereda `PBase`.

## Layouts candidatos

- `activity_anulacion` — `app/src/main/java/com/dtsgt/mpos/Anulacion.java:148`.

## Navegación candidata

- `srvInventConfirm` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Anulacion.java:304`; condiciones en catálogo.
- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Anulacion.java:704`; condiciones en catálogo.
- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Anulacion.java:1302`; condiciones en catálogo.
- `CuponFisicoEnvios` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Anulacion.java:2373`; condiciones en catálogo.

## Estado global escrito

`autocom`, `dias_anul`, `timeout`, `validimp`, `wsurl`

## Tablas mencionadas estáticamente

`D_COBRO`, `D_COBROD`, `D_COBROP`, `D_CUPON_ACTIV`, `D_CXC`, `D_DEPOS`, `D_DEPOSB`, `D_DEPOSD`, `D_FACTURA`, `D_FACTURACOR`, `D_FACTURAD`, `D_FACTURAP`, `D_FACTURAS`, `D_FACTURA_ANULACION`, `D_FEL_ERROR`, `D_MOV`, `D_MOVD`, `D_MOVDB`, `D_NOTACRED`, `D_PEDIDO`, `D_PEDIDOD`, `FINDIA`, `P_BANCO`, `P_CLIENTE`, `P_COREL`, `P_ENCABEZADO_REPORTESHH`, `P_PRODUCTO`, `P_STOCK`, `T_COSTO`

## Métodos

- `onCreate` — línea 144.
- `confirmaInventario` — línea 302.
- `doClear` — línea 313.
- `doDocuments` — línea 317.
- `anulDoc` — línea 321.
- `setHandlers` — línea 385.
- `onSwipeRight` — línea 389.
- `onSwipeLeft` — línea 392.
- `onCheckedChanged` — línea 430.
- `afterTextChanged` — línea 438.
- `beforeTextChanged` — línea 440.
- `onTextChanged` — línea 442.
- `listItems` — línea 456.
- `anulDocument` — línea 646.
- `msgAskFacturaSAT` — línea 713.
- `wsCallBack` — línea 723.
- `felCallBack` — línea 754.
- `anulacionFEL` — línea 768.
- `felCallBackInfile` — línea 778.
- `buildAnulXML` — línea 809.
- `Get_NIT_Cliente` — línea 848.
- `anulacionFELSal` — línea 874.
- `felCallBackInfileSal` — línea 939.
- `anulacionFELPana` — línea 1001.
- `felCallBackInfilePana` — línea 1023.
- `envioFactura` — línea 1047.
- `wsCallBackGT` — línea 1081.
- `guardaError` — línea 1111.
- `processComplete` — línea 1137.
- `statusFactura` — línea 1147.
- `anulPedido` — línea 1171.
- `anulFactura` — línea 1188.
- `enviaAnulaciones` — línea 1295.
- `processAnul` — línea 1312.
- `revertProd` — línea 1335.
- `revertProd` — línea 1353.
- `revertProdTallaColor` — línea 1357.
- `anulDepos` — línea 1597.
- `anulDeposParc` — línea 1652.
- `anulRecarga` — línea 1662.
- `anulDevol` — línea 1703.
- `anulRecib` — línea 1748.
- `anulNotaCredito` — línea 1762.
- `tieneFacturaNC` — línea 1806.
- `tieneNotaCredFactura` — línea 1829.
- `ExisteFactura` — línea 1852.
- `ImpresionFactura` — línea 1874.
- `Impresion` — línea 1882.
- `ImprimeNC_Fact` — línea 1891.
- `askPrint` — línea 1928.
- `showDateDialog1` — línea 2021.
- `showDateDialog2` — línea 2032.
- `obtenerFecha` — línea 2043.
- `setFechaAct` — línea 2111.
- `aprLoadHeadData` — línea 2133.
- `buildHeader` — línea 2183.
- `saveHeadLines` — línea 2199.
- `encabezado` — línea 2234.
- `loadHeadLines` — línea 2297.
- `enviaCuponesFisicos` — línea 2330.
- `tieneCuponFisico` — línea 2351.
- `cargaCuponesFisicos` — línea 2370.
- `anulaCupon` — línea 2379.
- `cbAnulaCupon` — línea 2395.
- `showMenu` — línea 2411.
- `getURL` — línea 2442.
- `msgAsk` — línea 2473.
- `checkFactDepos` — línea 2499.
- `valexist` — línea 2521.
- `valexist2` — línea 2540.
- `msgAnul` — línea 2560.
- `onClick` — línea 2568.
- `validaPagoCupon` — línea 2577.
- `onResume` — línea 2610.
- `onBackPressed` — línea 2627.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

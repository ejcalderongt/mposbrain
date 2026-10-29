# WSEnv

Dominio: `sync-configuration`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/WSEnv.java:60`; hereda `PBase`.

## Layouts candidatos

- `activity_w_s_env` — `app/src/main/java/com/dtsgt/mpos/WSEnv.java:131`.

## Navegación candidata

- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/WSEnv.java:656`; condiciones en catálogo.

## Estado global escrito

`codigo_proveedor`

## Tablas mencionadas estáticamente

`D_BARRIL_TRANS`, `D_CXC`, `D_FACTURA`, `D_FACTURAC`, `D_FACTURACOR`, `D_FACTURAD`, `D_FACTURAD_TC`, `D_FACTURAHN`, `D_FACTURAP`, `D_FACTURAPR`, `D_FACTURA_FEL_PAIS`, `D_FACTURA_SV`, `D_FEL_BITACORA`, `D_FEL_ERROR`, `D_MOV`, `D_MOVD`, `D_MOVD_ALMACEN`, `D_MOV_ALMACEN`, `D_ORDEN_STAT`, `D_PRECUENTA_DET`, `D_PRECUENTA_ENC`, `D_PRECUENTA_FACTURA`, `D_USUARIO_ASISTENCIA`, `P_CAJACIERRE`, `P_CAJAPAGOS`, `P_CAJAREPORTE`, `P_CLIENTE`, `P_CLIENTE_DIR`, `P_COREL`, `P_DEPOSITO`, `P_PRODUCTO`, `P_PROVEEDOR_SUCURSAL`, `P_STOCK`, `P_SUCURSAL`, `T_COSTO`, `T_FEL_SV_ERROR`, `T_VENTA_HORA`

## Métodos

- `onCreate` — línea 128.
- `doStart` — línea 203.
- `doStartClean` — línea 214.
- `wsCallBack` — línea 344.
- `execws` — línea 458.
- `processComplete` — línea 530.
- `finEnvio` — línea 556.
- `limpiaTablas` — línea 620.
- `enviaAnulaciones` — línea 649.
- `pendientesNotasEnvio` — línea 670.
- `processFactura` — línea 694.
- `addFactheader` — línea 854.
- `addPropinaItem` — línea 930.
- `addFacturaCorItem` — línea 948.
- `D_factCaddItemSql` — línea 967.
- `D_factRaddItemSql` — línea 983.
- `D_fact_fel_paisItemSql` — línea 995.
- `D_fact_dTCaddItemSql` — línea 1035.
- `statusFactura` — línea 1051.
- `processClients` — línea 1076.
- `statusClients` — línea 1109.
- `processMov` — línea 1133.
- `statusMov` — línea 1181.
- `processMovAlmacen` — línea 1205.
- `statusMovAlmacen` — línea 1247.
- `processPrecuentas` — línea 1273.
- `statusPrecuentas` — línea 1305.
- `processPrecuentasFact` — línea 1331.
- `statusPrecuentasFact` — línea 1354.
- `processAnul` — línea 1378.
- `processCajaCierre` — línea 1395.
- `statusCajaCierre` — línea 1426.
- `preparaCorCierre` — línea 1458.
- `processCorCierre` — línea 1487.
- `processCajaPagos` — línea 1495.
- `statusCajaPagos` — línea 1532.
- `processCajaReporte` — línea 1560.
- `statusCajaReporte` — línea 1588.
- `processStock` — línea 1620.
- `statusStock` — línea 1634.
- `processFelBita` — línea 1662.
- `statusFelBita` — línea 1689.
- `processAsist` — línea 1701.
- `asistaddItemSql` — línea 1733.
- `statusAsist` — línea 1756.
- `processCosto` — línea 1770.
- `statusCosto` — línea 1785.
- `processFELErr` — línea 1794.
- `statusFELErr` — línea 1809.
- `processCxC` — línea 1818.
- `statusCxC` — línea 1833.
- `processDeposito` — línea 1842.
- `statusDeposito` — línea 1865.
- `processOrdStat` — línea 1874.
- `statusOrdStat` — línea 1890.
- `processProvLoc` — línea 1899.
- `statusProvLoc` — línea 1916.
- `generaDatosVentaHora` — línea 1930.
- `ventaHoraCallback` — línea 1953.
- `tieneDatosVentaHora` — línea 1995.
- `preparaEnvio` — línea 2009.
- `updateLabel` — línea 2214.
- `run` — línea 2217.
- `ajustaFormatoPagos` — línea 2224.
- `addUpdateItem` — línea 2236.
- `addCostoItemSql` — línea 2256.
- `addCxCItemSql` — línea 2271.
- `addCostoUpdProdSql` — línea 2294.
- `addFELErrItemSql` — línea 2299.
- `removeNonAlphanumeric` — línea 2330.
- `addPrecEncItemSql` — línea 2334.
- `addPrecDetItemSql` — línea 2352.
- `addPrecFactItemSql` — línea 2372.
- `addDepositoItemSql` — línea 2386.
- `addOrdStatItemSql` — línea 2412.
- `addProvLocItemSql` — línea 2429.
- `addClienteItemSql` — línea 2442.
- `msgboxwait` — línea 2482.
- `onBackPressed` — línea 2516.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

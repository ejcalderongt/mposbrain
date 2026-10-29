# ComWS

Dominio: `sync-configuration`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/ComWS.java:81`; hereda `PBase`.

## Layouts candidatos

- `activity_com_ws` — `app/src/main/java/com/dtsgt/mpos/ComWS.java:139`.

## Navegación candidata

- `ComWSFotos` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ComWS.java:319`; condiciones en catálogo.
- `ComWSExist` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ComWS.java:404`; condiciones en catálogo.
- `ComWSPrec` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ComWS.java:415`; condiciones en catálogo.
- `ComWSRec` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ComWS.java:426`; condiciones en catálogo.
- `this.getPackageName` (external_app_candidate) — `app/src/main/java/com/dtsgt/mpos/ComWS.java:4089`; condiciones en catálogo.

## Estado global escrito

`peModal`, `peStockItf`

## Tablas mencionadas estáticamente

`D_ATENCION`, `D_CLICOORD`, `D_CLINUEVO`, `D_CLINUEVO_APR`, `D_COBRO`, `D_CXC`, `D_DEPOS`, `D_FACTURA`, `D_MOV`, `D_MOVD`, `D_MOVDB`, `D_NOTACRED`, `D_PEDIDO`, `D_RATING`, `D_REPFINDIA`, `D_SOLICINV`, `D_SOLICINVD`, `FINDIA`, `LIC_CLIENTE`, `O_LINEA`, `O_PROD`, `O_RUTA`, `PARAMS`, `P_ARCHIVOCONF`, `P_BANCO`, `P_BITACORA_VERSIONHH`, `P_BONIF`, `P_CLIENTE`, `P_COREL`, `P_CORREL_OTROS`, `P_DESCUENTO`, `P_DEVOLUCIONES_SAP`, `P_DOC_ENVIADOS_HH`, `P_EMPRESA`, `P_ENCABEZADO_REPORTESHH`, `P_ENCABEZADO_REPORTESHH_II`, `P_FACTORCONV`, `P_IMPUESTO`, `P_LINEA`, `P_MEDIAPAGO`, `P_MONEDA`, `P_NIVELPRECIO`, `P_PARAMEXT`, `P_PRODMENU`, `P_PRODOPC`, `P_PRODOPCLIST`, `P_PRODPRECIO`, `P_PRODUCTO`, `P_PROVEEDOR`, `P_RUTA`, `P_STOCK`, `P_SUCURSAL`, `VENDEDORES`

## Métodos

- `onCreate` — línea 135.
- `run` — línea 238.
- `askRec` — línea 252.
- `askSend` — línea 272.
- `onClick` — línea 286.
- `askActualize` — línea 304.
- `doFotos` — línea 318.
- `setHandlers` — línea 322.
- `onSwipeRight` — línea 324.
- `onSwipeLeft` — línea 328.
- `runRecep` — línea 337.
- `runSend` — línea 377.
- `runExist` — línea 401.
- `runPrecios` — línea 412.
- `runRecarga` — línea 423.
- `writeData` — línea 434.
- `validaPendientes` — línea 450.
- `fillTable` — línea 475.
- `commitSQL` — línea 557.
- `actualize` — línea 616.
- `OpenDTt` — línea 672.
- `getTest` — línea 726.
- `envioFachada` — línea 760.
- `checkLicence` — línea 802.
- `checkLicenceRuta` — línea 840.
- `guardaImagen` — línea 878.
- `getData` — línea 935.
- `procesaParamsExt` — línea 1124.
- `Actualiza_FinDia` — línea 1194.
- `update_Corel_GrandTotal` — línea 1198.
- `AddTable` — línea 1203.
- `AddTableVL` — línea 1232.
- `getTableSQL` — línea 1260.
- `getTableSQLOrig` — línea 1417.
- `comparaCorrel` — línea 1470.
- `FinDia` — línea 1515.
- `ActualizaStatcom` — línea 1549.
- `encodeLicence` — línea 1580.
- `encodeLicenceRuta` — línea 1593.
- `validaLicencia` — línea 1606.
- `wsExecute` — línea 1644.
- `wsFinished` — línea 1673.
- `sendData` — línea 1763.
- `envioFacturas` — línea 1828.
- `sendFotoCli` — línea 1917.
- `sendFotoProd` — línea 1949.
- `sendFotoFamilia` — línea 1981.
- `sendFoto` — línea 2013.
- `envioPedidos` — línea 2089.
- `envioCobros` — línea 2167.
- `envioNotasCredito` — línea 2243.
- `envioNotasDevolucion` — línea 2319.
- `envioDepositos` — línea 2405.
- `Get_Corel_D_Mov` — línea 2477.
- `envio_D_MOV` — línea 2499.
- `envioCli` — línea 2590.
- `envioAtten` — línea 2670.
- `envioCoord` — línea 2724.
- `envioSolicitud` — línea 2780.
- `envioFinDia` — línea 2852.
- `envioRating` — línea 2897.
- `updateAcumulados` — línea 2960.
- `updateLicence` — línea 2988.
- `addItem` — línea 3015.
- `updateLicencePush` — línea 3032.
- `Actualiza` — línea 3049.
- `actArchConfig` — línea 3090.
- `actProdOpcList` — línea 3117.
- `actProdOpc` — línea 3148.
- `actProdMenu` — línea 3180.
- `actSucursal` — línea 3210.
- `actProveedor` — línea 3242.
- `actProdprecio` — línea 3269.
- `actParamext` — línea 3296.
- `actFactorconv` — línea 3323.
- `actProducto` — línea 3350.
- `actMoneda` — línea 3377.
- `actNivelPrecio` — línea 3404.
- `actBanco` — línea 3431.
- `actCaja` — línea 3460.
- `actCliente` — línea 3487.
- `actDesc` — línea 3514.
- `actEmpresa` — línea 3541.
- `actFamilia` — línea 3568.
- `actImpuesto` — línea 3595.
- `actMedia` — línea 3622.
- `wsSendExecute` — línea 3654.
- `wsSendFinished` — línea 3678.
- `sendConfirm` — línea 3773.
- `run` — línea 3800.
- `wsConfirmExecute` — línea 3817.
- `wsConfirmFinished` — línea 3840.
- `setComParams` — línea 3892.
- `getDocCount` — línea 3915.
- `getMac` — línea 3945.
- `ultCorel` — línea 3951.
- `ultSerie` — línea 3973.
- `Get_Fecha_Inventario` — línea 3996.
- `ultimoCierreFecha` — línea 4023.
- `visibilidadBotones` — línea 4040.
- `paramsExtra` — línea 4057.
- `writeErrLog` — línea 4067.
- `restartApp` — línea 4086.
- `ExistenDatosSinEnviar` — línea 4101.
- `ExisteInventario` — línea 4125.
- `ExistenDatos` — línea 4145.
- `BorraDatosAnteriores` — línea 4169.
- `onClick` — línea 4178.
- `onClick` — línea 4185.
- `SetStatusRecTo` — línea 4196.
- `SetStatusRecToTrans` — línea 4210.
- `GetStatusRec` — línea 4220.
- `Eliminatablas` — línea 4242.
- `puedeComunicar` — línea 4263.
- `getWSUrl` — línea 4286.
- `askSendCorrect` — línea 4314.
- `onClick` — línea 4324.
- `onClick` — línea 4330.
- `askIncorrect` — línea 4343.
- `onClick` — línea 4353.
- `onClick` — línea 4359.
- `askOk` — línea 4372.
- `onClick` — línea 4386.
- `askOkCom` — línea 4400.
- `onClick` — línea 4414.
- `onClick` — línea 4420.
- `msgResultEnvio` — línea 4434.
- `onClick` — línea 4443.
- `msgAskExit` — línea 4455.
- `onClick` — línea 4464.
- `msgAskExitComplete` — línea 4484.
- `onClick` — línea 4493.
- `onClick` — línea 4499.
- `msgAskConfirmaRecibido` — línea 4512.
- `onClick` — línea 4520.
- `msgAskSinLicencia` — línea 4534.
- `onClick` — línea 4543.
- `msgFinEnvio` — línea 4556.
- `onClick` — línea 4565.
- `msgAskActualiza` — línea 4577.
- `onClick` — línea 4584.
- `onBackPressed` — línea 4600.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

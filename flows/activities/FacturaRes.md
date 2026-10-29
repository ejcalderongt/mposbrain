# FacturaRes

Dominio: `restaurant`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:138`; hereda `PBase`.

## Layouts candidatos

- `activity_factura_res_precue` — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:281`.
- `activity_factura_res_ver_precue` — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:283`.
- `activity_factura_res` — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:288`.
- `activity_factura_res_port` — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:291`.
- `activity_factura_res_ver` — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:293`.

## Navegación candidata

- `Pago` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:642`; condiciones en catálogo.
- `PagoTarjeta` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:693`; condiciones en catálogo.
- `BonVenta` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:803`; condiciones en catálogo.
- `FELFactura` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:1251`; condiciones en catálogo.
- `FELFactura` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:1255`; condiciones en catálogo.
- `FELFacturaSV` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:1257`; condiciones en catálogo.
- `FELFacturaPana` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:1259`; condiciones en catálogo.
- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:1487`; condiciones en catálogo.
- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:3348`; condiciones en catálogo.
- `CuponPagos` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:5264`; condiciones en catálogo.
- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:5701`; condiciones en catálogo.
- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:6589`; condiciones en catálogo.
- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:6876`; condiciones en catálogo.
- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:6904`; condiciones en catálogo.
- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:6916`; condiciones en catálogo.
- `DescMonto` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:7576`; condiciones en catálogo.
- `DescMonto` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FacturaRes.java:7815`; condiciones en catálogo.

## Estado global escrito

`InvCompSend`, `QRCodeStr`, `autocom`, `brw`, `cliente_lealtad`, `cliposflag`, `cobroPendiente`, `codigo_cliente`, `corel_pago`, `cupon_canje_pagado`, `delivery`, `desc_monto`, `descadd`, `dom_nom`, `domicilio`, `dvbrowse`, `fact_corel`, `felcorel`, `gCorreoCliente`, `gDirCliente`, `gNITCliente`, `gNombreCliente`, `impStarCutPaper`, `impresion_comanda`, `iniciaVenta`, `mesanom`, `mesero_venta`, `modo_cortesia`, `monto_propina`, `nit_tipo`, `nombre_cortesia`, `nombre_mesero`, `nota_envio_corel`, `nota_envio_modo`, `numero_orden`, `numero_orden_prec`, `nummesapedido`, `ordcorel`, `pagocobro`, `pagolim`, `pagoval`, `peMFact`, `pePropinaCarta`, `ped_dom_cambio`, `ped_dom_cliente`, `ped_dom_dir`, `ped_dom_orden`, `ped_dom_tel`, `ped_dom_texto`, `pedido_dom_import`, `percepcion`, `propina_vacia`, `reinicia_venta`, `sal_iddep`, `sal_idmun`, `sal_idneg`, `sin_propina`, `sinimp`, `tiponcredito`, `total_factura_previo_descuento`, `total_pago`, `usuario_cortesia`, `vendnom`, `ventalock`

## Tablas mencionadas estáticamente

`D_BARRIL_TRANS`, `D_BONIF_LOTES`, `D_CXC`, `D_FACTURA`, `D_FACTURACOR`, `D_FACTURAR`, `D_FACTURA_EQUIPO`, `D_FACT_LOG`, `D_LEAL_CAMBIO`, `D_MOVD`, `D_NOTACRED`, `D_NOTAENVIO`, `D_NOTAENVIOD`, `D_ORDEN`, `D_ORDEND`, `D_PRECUENTA_DET`, `D_PRECUENTA_ENC`, `D_PRECUENTA_FACTURA`, `P_CLIENTE`, `P_COREL`, `P_IMPUESTO`, `P_LINEA`, `P_MEDIAPAGO`, `P_PRODUCTO`, `P_RES_SESION`, `P_STOCK`, `T_BONITEM`, `T_COMANDA`, `T_COMBO`, `T_FACTRECETA`, `T_LEAL_CRITERIA`, `T_LEAL_ITEMS`, `T_LEAL_PUNTOS`, `T_ORDEN_ING`, `T_ORDEN_MOD`, `T_PAGO`, `T_RES_SESSION_COR`, `T_VENTA`, `T_VENTA_HORA`, `T_VENTA_ING`, `T_VENTA_MOD`, `T_VENTA_TALLA`

## Métodos

- `tracePropina` — línea 143.
- `onPause` — línea 174.
- `onDestroy` — línea 179.
- `onCreate` — línea 269.
- `run` — línea 485.
- `prevScreen` — línea 612.
- `paySelect` — línea 626.
- `payCash` — línea 652.
- `payCard` — línea 673.
- `payCred` — línea 703.
- `pendientePago` — línea 728.
- `delPay` — línea 735.
- `doDesc` — línea 739.
- `prnCuenta` — línea 763.
- `prnCuentaSin` — línea 784.
- `showBon` — línea 801.
- `DaVuelto` — línea 811.
- `doPropina` — línea 820.
- `pago100` — línea 825.
- `pago50` — línea 834.
- `pago20` — línea 843.
- `pago10` — línea 852.
- `pago5` — línea 861.
- `doKey` — línea 870.
- `setHandlers` — línea 881.
- `onSwipeRight` — línea 886.
- `onSwipeLeft` — línea 889.
- `afterTextChanged` — línea 898.
- `beforeTextChanged` — línea 900.
- `onTextChanged` — línea 902.
- `onKey` — línea 909.
- `processFinalPromo` — línea 938.
- `updDesc` — línea 968.
- `totalOrder` — línea 979.
- `fillTotals` — línea 1047.
- `finishOrder` — línea 1199.
- `impresionDocumento` — línea 1271.
- `cargaTotalesHonduras` — línea 1507.
- `cargaTotalesSalvador` — línea 1529.
- `saveOrder` — línea 1551.
- `rebajaStockUM` — línea 2917.
- `rebajaStockUM2` — línea 2935.
- `rebajaStockBonif` — línea 2988.
- `rebajaStockTallaColor` — línea 3106.
- `agregaMasVendidos` — línea 3129.
- `creaTextoDomicilio` — línea 3148.
- `splitText` — línea 3165.
- `saveAtten` — línea 3174.
- `totalDescProd` — línea 3228.
- `esProductoConStock` — línea 3260.
- `esProductoConStock` — línea 3286.
- `cbCargaResSessID` — línea 3310.
- `enviaFacturaEnquipo` — línea 3330.
- `completaEstadoOrden` — línea 3363.
- `fbocLista` — línea 3403.
- `marcarArticulosPagados` — línea 3417.
- `todasCuentasPagadas` — línea 3430.
- `cuentaPagada` — línea 3447.
- `borrarCuentas` — línea 3458.
- `run` — línea 3472.
- `fbocDel` — línea 3499.
- `borrarBloqueo` — línea 3525.
- `assignCorel` — línea 3546.
- `assignCorelFactura` — línea 3580.
- `assignCorelCredito` — línea 3711.
- `assignCorelTicket` — línea 3763.
- `procesaInventario` — línea 3821.
- `agregaCombo` — línea 3853.
- `agregaReceta` — línea 3863.
- `agregaProductoReceta` — línea 3885.
- `inventarioRecetas` — línea 3898.
- `existenciaReceta` — línea 3933.
- `existenciaComboItem` — línea 3940.
- `listaCortesias` — línea 3951.
- `onClick` — línea 3974.
- `onClick` — línea 3981.
- `aplicaCortesia` — línea 4007.
- `completaEstadoOrdenCortesia` — línea 4029.
- `totalOrderCortesia` — línea 4041.
- `guardaCortesia` — línea 4085.
- `impresionCortesia` — línea 4220.
- `impresionEncabezado` — línea 4296.
- `impresionDetalle` — línea 4317.
- `prepareExplicitTipPrint` — línea 4352.
- `buildPrecuentaSafely` — línea 4368.
- `impresionCuenta` — línea 4391.
- `run` — línea 4461.
- `registroPrecuenta` — línea 4475.
- `impresionCuentaxxxx` — línea 4539.
- `run` — línea 4616.
- `inputEfectivo` — línea 4634.
- `onClick` — línea 4651.
- `onClick` — línea 4661.
- `inputVuelto` — línea 4675.
- `onClick` — línea 4716.
- `onClick` — línea 4751.
- `msgAskVuelto` — línea 4770.
- `Davuelto` — línea 4798.
- `vuelto` — línea 4832.
- `onClick` — línea 4842.
- `validaPagoEfectivo` — línea 4855.
- `applyCash` — línea 4906.
- `applyPendiente` — línea 4967.
- `inputCredito` — línea 5017.
- `onClick` — línea 5037.
- `onClick` — línea 5047.
- `applyCredit` — línea 5062.
- `inputCard` — línea 5107.
- `onClick` — línea 5122.
- `onClick` — línea 5128.
- `checkNum` — línea 5141.
- `addPagoTar` — línea 5162.
- `checkPago` — línea 5191.
- `processPagosCupon` — línea 5259.
- `terminaPagosCupon` — línea 5271.
- `checkPagoEnvio` — línea 5284.
- `totalPago` — línea 5299.
- `checkPagoNF` — línea 5323.
- `pagoPendiente` — línea 5375.
- `androidid` — línea 5442.
- `validaMontoMaximo` — línea 5457.
- `imprimeComanda` — línea 5473.
- `divideComanda` — línea 5484.
- `generaArchivos` — línea 5537.
- `codigoProducto` — línea 5649.
- `agregaComanda` — línea 5672.
- `generaOrdenDespacho` — línea 5692.
- `generaOrdenEncabezado` — línea 5712.
- `generaOrdenDetalle` — línea 5743.
- `addProducto` — línea 5784.
- `addOrdedEncItemSql` — línea 5800.
- `tiempoProd` — línea 5822.
- `tiempoPreparacion` — línea 5832.
- `corelNotaEnvio` — línea 5860.
- `cbCorelNotaEnvio` — línea 5882.
- `run` — línea 5885.
- `actualizaNotaEnvio` — línea 5903.
- `cbActualizaNotaEnvio` — línea 5927.
- `llamaImpresion` — línea 5944.
- `showMsg` — línea 5964.
- `run` — línea 5967.
- `run` — línea 5970.
- `ActualizaNotaEnvio` — línea 5979.
- `calculaPuntos` — línea 5998.
- `filtrarCriteriaPuntos` — línea 6010.
- `calculaPuntosTotales` — línea 6049.
- `aplicaPuntos` — línea 6131.
- `porMulti` — línea 6237.
- `porRango` — línea 6261.
- `consultaPuntos` — línea 6283.
- `cbConsultaPuntos` — línea 6297.
- `clearGlobals` — línea 6328.
- `checkPromo` — línea 6346.
- `cliPorDia` — línea 6361.
- `prodPorPeso` — línea 6365.
- `codigoPagoBilletera` — línea 6374.
- `permiteTarjeta` — línea 6388.
- `marcaFacturaContingencia` — línea 6402.
- `impresionCuenta2` — línea 6441.
- `run` — línea 6510.
- `completaEstadoOrden2` — línea 6524.
- `broadcastJournalFlag` — línea 6557.
- `broadcastJournalCuenta` — línea 6607.
- `todasCuentasPagadas2` — línea 6675.
- `impresionCuenta3` — línea 6701.
- `run` — línea 6761.
- `estadoCuenta` — línea 6775.
- `enviaAviso` — línea 6803.
- `getProd` — línea 6828.
- `pantallaPortrait` — línea 6841.
- `pantallaHorizontal` — línea 6852.
- `enviaPago` — línea 6866.
- `marcaPagoCuenta` — línea 6886.
- `enviaPrecuenta` — línea 6902.
- `enviaEstado` — línea 6914.
- `agregaRegistroBarril` — línea 6926.
- `tipoNIT` — línea 6956.
- `corelPrecuenta` — línea 6987.
- `getCorelPrecuenta` — línea 7016.
- `validaNIT` — línea 7039.
- `creditoDisp` — línea 7115.
- `validaPagoCupon` — línea 7144.
- `aplicaDescuentoHonduras` — línea 7179.
- `askSave` — línea 7200.
- `askSave` — línea 7209.
- `askSavePos` — línea 7228.
- `askPendientePago` — línea 7269.
- `askPrint` — línea 7289.
- `askDelPago` — línea 7369.
- `askPrecuenta` — línea 7395.
- `msgAskComanda` — línea 7418.
- `msgAskSend` — línea 7428.
- `ingresaPropina` — línea 7437.
- `msgAskSinPropina` — línea 7469.
- `valorDescuentoMonto` — línea 7479.
- `msgAskCredito` — línea 7506.
- `onClick` — línea 7513.
- `onClick` — línea 7521.
- `msgAskCreditoSin` — línea 7528.
- `onClick` — línea 7535.
- `onClick` — línea 7542.
- `validaSupervisor` — línea 7549.
- `askNotaEnviox` — línea 7599.
- `askNotaEnvio` — línea 7628.
- `askPropina` — línea 7654.
- `askPropinaSin` — línea 7678.
- `showDescHondMenu` — línea 7700.
- `onItemClick` — línea 7718.
- `onClick` — línea 7748.
- `onResume` — línea 7767.
- `onBackPressed` — línea 7866.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

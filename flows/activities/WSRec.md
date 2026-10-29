# WSRec

Dominio: `sync-configuration`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/WSRec.java:137`; hereda `PBase`.

## Layouts candidatos

- `activity_wsrec` — `app/src/main/java/com/dtsgt/mpos/WSRec.java:171`.

## Navegación candidata

- `ValidCorel` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/WSRec.java:1521`; condiciones en catálogo.
- `ValidCorel` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/WSRec.java:5208`; condiciones en catálogo.
- `com.dts.mposupd` (external_app_candidate) — `app/src/main/java/com/dtsgt/mpos/WSRec.java:5225`; condiciones en catálogo.
- `this.getPackageName` (external_app_candidate) — `app/src/main/java/com/dtsgt/mpos/WSRec.java:5377`; condiciones en catálogo.

## Estado global escrito

`Sincronizar_Clientes`, `clave`, `emp`, `estado_recep`, `timeout`, `wsurl`

## Tablas mencionadas estáticamente

`D_ORDEN_LOG`, `P_ALMACEN`, `P_ARCHIVOCONF`, `P_BANCO`, `P_BARRIL_BARRA`, `P_BARRIL_TIPO`, `P_BONIF`, `P_CAJA_IMPRESORA`, `P_CLIENTE`, `P_CONCEPTOPAGO`, `P_COREL`, `P_CORTESIA`, `P_DEPARTAMENTO`, `P_DESCUENTO`, `P_EMPRESA`, `P_EMPRESA_TRANS`, `P_EMPRESA_TRANSPORTE`, `P_ENCABEZADO_REPORTESHH`, `P_FACTORCONV`, `P_FEL_IMPUESTO`, `P_FRASE`, `P_GIRO_NEGOCIO`, `P_HOTEL_BRAZALETE`, `P_IMPRESORA`, `P_IMPRESORA_MARCA`, `P_IMPRESORA_MODELO`, `P_IMPRESORA_REDIRECCION`, `P_IMPUESTO`, `P_LEALTAD_BILLETERA_CAMBIO`, `P_LEALTAD_PUNTOS_VIGENCIA`, `P_LEAL_CRITERIA`, `P_LEAL_PUNTOS`, `P_LINEA`, `P_LINEA_IMPRESORA`, `P_MEDIAPAGO`, `P_MENUOPCIONES_ROL`, `P_MODIFICADOR`, `P_MODIFICADOR_GRUPO`, `P_MODULOS_ROL`, `P_MONEDA`, `P_MOTIVO_AJUSTE`, `P_MUNICIPIO`, `P_NIVELPRECIO`, `P_NIVELPRECIO_SUCURSAL`, `P_OBJETIVO`, `P_PARAMEXT`, `P_PRODCLASIFMODIF`, `P_PRODCOMBO`, `P_PRODMENU`, `P_PRODMENUOPC`, `P_PRODMENUOPC_DET`, `P_PRODPRECIO`, `P_PRODPRECIOESP`, `P_PRODPRECIO_TALLA_COLOR`, `P_PRODRECETA`, `P_PRODUCTO`, `P_PRODUCTO_COLOR`, `P_PRODUCTO_TALLA_COLOR`, `P_PRODUCTO_TIPO`, `P_PROVEEDOR`, `P_REGLA_COSTO`, `P_RES_GRUPO`, `P_RES_MESA`, `P_RES_SALA`, `P_RUTA`, `P_SUCURSAL`, `P_TIPONEG`, `P_TIPO_CONTRIBUYENTE`, `P_UNIDAD`, `P_UNIDAD_CONV`, `P_USGRUPO`, `P_USGRUPOOPC`, `P_USOPCION`, `P_VENDEDOR_ROL`, `P_VENDEDOR_SUCURSAL`, `T_IPBYPASS`, `VENDEDORES`

## Métodos

- `onCreate` — línea 166.
- `doStart` — línea 276.
- `wsCallBack` — línea 510.
- `execws` — línea 902.
- `run` — línea 1065.
- `setHandlers` — línea 1074.
- `onKey` — línea 1079.
- `onKey` — línea 1099.
- `onFocusChange` — línea 1123.
- `run` — línea 1136.
- `onKey` — línea 1148.
- `Recibir` — línea 1177.
- `processComplete` — línea 1201.
- `processData` — línea 1223.
- `processDataFinal` — línea 1262.
- `run` — línea 1265.
- `validaCombos` — línea 1306.
- `printBypass` — línea 1335.
- `productoPropinaServicio` — línea 1382.
- `limpiaArchivosCierre` — línea 1451.
- `mostrarListaCombo` — línea 1491.
- `onItemClick` — línea 1502.
- `onClick` — línea 1511.
- `fechaContratoFEL` — línea 1531.
- `updateFechaContrato` — línea 1541.
- `aplicaAmbienteSV` — línea 1587.
- `aplicaAmbientePA` — línea 1622.
- `ajusteRedireccion` — línea 1651.
- `validaFEL` — línea 1660.
- `processEmpresas` — línea 1697.
- `processBancos` — línea 1768.
- `processMotivoAjustes` — línea 1806.
- `processDepartamentos` — línea 1844.
- `processMunicipios` — línea 1881.
- `processProductoTipo` — línea 1918.
- `processConfig` — línea 1953.
- `processBonif` — línea 1995.
- `processCorel` — línea 2048.
- `processDescuento` — línea 2095.
- `processFactor` — línea 2141.
- `processFrases` — línea 2175.
- `processImpuesto` — línea 2206.
- `processLinea` — línea 2239.
- `processCliente` — línea 2310.
- `processEncabezado` — línea 2392.
- `processMedia` — línea 2425.
- `processMoneda` — línea 2463.
- `processNivel` — línea 2499.
- `processCombo` — línea 2533.
- `processProdMenu` — línea 2573.
- `processOpciones` — línea 2611.
- `processOpcionesdet` — línea 2649.
- `processPrecios` — línea 2685.
- `processProveedores` — línea 2730.
- `processProductos` — línea 2775.
- `processRutas` — línea 2910.
- `processSucursales` — línea 2947.
- `processUsrGrupos` — línea 3011.
- `processUsrGrOpc` — línea 3046.
- `processGrOpciones` — línea 3081.
- `processVendedores` — línea 3115.
- `processConceptoPago` — línea 3192.
- `processParametrosExtra` — línea 3227.
- `processParametrosExtraRuta` — línea 3262.
- `addItemSqlParamExtRuta` — línea 3308.
- `processResSala` — línea 3321.
- `processResMesa` — línea 3364.
- `processResGrupo` — línea 3411.
- `processLineaImpresora` — línea 3450.
- `processImpresora` — línea 3488.
- `processMarcaImpresora` — línea 3534.
- `processModeloImpresora` — línea 3570.
- `processVersion` — línea 3607.
- `processCajaImpresora` — línea 3627.
- `processUnidad` — línea 3665.
- `processUnidadConv` — línea 3699.
- `processProdReceta` — línea 3735.
- `processNivelSucursal` — línea 3774.
- `processReglaCosto` — línea 3815.
- `processAlmacen` — línea 3851.
- `processModificador` — línea 3890.
- `processModificadorGrupo` — línea 3926.
- `processProdClasifModif` — línea 3961.
- `processBarrilTipo` — línea 3996.
- `processBarrilBarra` — línea 4035.
- `processCortesia` — línea 4072.
- `processVendedorRol` — línea 4110.
- `processVendedorSucursal` — línea 4151.
- `processTipoNegocio` — línea 4192.
- `processImpresoraRedir` — línea 4232.
- `processGiroNegocio` — línea 4269.
- `iniciaWebAPIStream` — línea 4309.
- `StreamNext` — línea 4320.
- `StreamCallBack` — línea 4378.
- `terminaWebAPIStream` — línea 4406.
- `run` — línea 4408.
- `failWebAPIStream` — línea 4420.
- `cbMenuVendedorRol` — línea 4432.
- `cbMenuModuloRol` — línea 4455.
- `cbMenuOpcionesRol` — línea 4484.
- `cbCostoMetodo` — línea 4513.
- `cbPreciosEspeciales` — línea 4536.
- `cbObjetivos` — línea 4578.
- `cbLealtadPuntos` — línea 4621.
- `cbLealtadCriteria` — línea 4669.
- `cbTallaColorPrecios` — línea 4708.
- `cbProductoColores` — línea 4742.
- `cbTallaColor` — línea 4772.
- `cbCuponVigencia` — línea 4805.
- `cbBilleteraCambio` — línea 4836.
- `iniciaStream` — línea 4873.
- `terminaStream` — línea 4877.
- `llenaTipoContrib` — línea 4881.
- `tipoContrib` — línea 4900.
- `validaFechaContrato` — línea 4958.
- `empresaTransporte` — línea 4988.
- `hotelBrazalete` — línea 5046.
- `felImpuesto` — línea 5104.
- `updateLabel` — línea 5163.
- `run` — línea 5166.
- `run` — línea 5168.
- `updateLabel` — línea 5178.
- `run` — línea 5181.
- `msgboxwait` — línea 5187.
- `onClick` — línea 5195.
- `msgAskVersion` — línea 5217.
- `onClick` — línea 5223.
- `onClick` — línea 5235.
- `msgboxexit` — línea 5244.
- `onClick` — línea 5251.
- `validaDatos` — línea 5258.
- `run` — línea 5271.
- `run` — línea 5287.
- `run` — línea 5303.
- `validaParametros` — línea 5321.
- `guardaDatosConexion` — línea 5344.
- `restartApp` — línea 5374.
- `fechaActualizacion` — línea 5389.
- `paisEmpresa` — línea 5400.
- `validaFELESA_archivo` — línea 5414.
- `onSuccess` — línea 5437.
- `onFailure` — línea 5442.
- `onSuccess` — línea 5449.
- `onFailure` — línea 5459.
- `asignaValoresProductoBS` — línea 5470.
- `onBackPressed` — línea 5483.
- `onResume` — línea 5488.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

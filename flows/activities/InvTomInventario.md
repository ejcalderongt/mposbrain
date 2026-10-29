# InvTomInventario

Dominio: `inventory`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/InvTomInventario.java:41`; hereda `PBase`.

## Layouts candidatos

- `activity_inv_tom_inventario` — `app/src/main/java/com/dtsgt/mpos/InvTomInventario.java:118`.

## Navegación candidata

- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvTomInventario.java:1533`; condiciones en catálogo.

## Estado global escrito

`autocom`, `barra`, `corelmov`, `docnumMov`

## Tablas mencionadas estáticamente

`D_MOV`, `D_MOVD`, `D_MOVD_ALMACEN`, `D_MOV_ALMACEN`, `P_PRODUCTO`, `T_MOVD`, `T_MOVR`, `T_STOCK`

## Métodos

- `onCreate` — línea 114.
- `onResume` — línea 162.
- `enlazarControles` — línea 183.
- `inicializarObjetos` — línea 224.
- `configurarHandlers` — línea 249.
- `afterTextChanged` — línea 290.
- `beforeTextChanged` — línea 291.
- `onTextChanged` — línea 293.
- `onAgregarProducto` — línea 307.
- `onGuardarInventario` — línea 311.
- `onEnfocarBarra` — línea 322.
- `onEnfocarCantidad` — línea 328.
- `onEnfocarCosto` — línea 333.
- `onTeclaPresionada` — línea 338.
- `onSeleccionarUnidadMedida` — línea 360.
- `onIngresarNumeroDocumento` — línea 365.
- `onOcultarPanelProductos` — línea 370.
- `onBuscarProductos` — línea 374.
- `onLimpiarFiltroProductos` — línea 379.
- `doInterrupt` — línea 384.
- `doCancel` — línea 389.
- `refrescarListaDetalle` — línea 410.
- `dispProd` — línea 459.
- `agregarOActualizarItem` — línea 482.
- `actualizaExistenciasDetalle` — línea 558.
- `fbListItems` — línea 573.
- `cancelarInventario` — línea 586.
- `procesarBarra` — línea 681.
- `limpiarEntradaProducto` — línea 692.
- `buscarProductoPorBarra` — línea 701.
- `cargarProductoDesdeItemSeleccionado` — línea 741.
- `existenciaActual` — línea 770.
- `inicializarMenu` — línea 798.
- `nuevoItemMenu` — línea 819.
- `procesarOpcionMenu` — línea 827.
- `borrarLineaSeleccionada` — línea 849.
- `consultarDisponibilidadFirebase` — línea 866.
- `fbCallBack` — línea 879.
- `inicializarPanelProductos` — línea 892.
- `cargarListaProductos` — línea 896.
- `seleccionarProductoPorCodigo` — línea 927.
- `mostrarListaUnidades` — línea 966.
- `compararLecturaScanner` — línea 998.
- `pantallaHorizontal` — línea 1024.
- `convertirAUnidadBase` — línea 1034.
- `mostrarDialogoDocumento` — línea 1055.
- `confirmarGuardado` — línea 1081.
- `reConfirmarGuardado` — línea 1095.
- `confirmarBorrarTodo` — línea 1109.
- `msgAskInterrupt` — línea 1124.
- `holdalmacen` — línea 1145.
- `converUMBas` — línea 1241.
- `hold` — línea 1288.
- `msgAskExit` — línea 1362.
- `onClick` — línea 1369.
- `onClick` — línea 1375.
- `guardarInventario` — línea 1384.
- `updateStock` — línea 1542.
- `updateStockAlmacen` — línea 1584.
- `onBackPressed` — línea 1629.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

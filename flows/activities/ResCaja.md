# ResCaja

Dominio: `restaurant`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/ResCaja.java:49`; hereda `PBase`.

## Layouts candidatos

- `activity_res_caja` — `app/src/main/java/com/dtsgt/mpos/ResCaja.java:95`.

## Navegación candidata

- `Nowifi` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ResCaja.java:172`; condiciones en catálogo.
- `ResCliente` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ResCaja.java:905`; condiciones en catálogo.

## Estado global escrito

`EsVentaDelivery`, `cliente`, `codigo_cliente`, `contrib`, `cuenta_borrar`, `gCorreoCliente`, `gDirCliente`, `gNITCliente`, `gNITcf`, `gNombreCliente`, `media`, `mesa_codigo`, `mesanom`, `mesero_factura`, `mesero_venta`, `nivel`, `nocuenta_precuenta`, `numero_orden`, `numero_orden_prec`, `nummesapedido`, `ordcorel`, `percepcion`, `precuenta_cuenta`, `pricuenta`, `primesa`, `propina_vacia`, `rutatipo`, `scancliente`, `timeout`, `ventalock`, `wsurl`

## Tablas mencionadas estáticamente

`P_CLIENTE`, `T_COMBO`, `T_VENTA`

## Métodos

- `onCreate` — línea 90.
- `doAdd` — línea 163.
- `doSincon` — línea 171.
- `doExit` — línea 175.
- `setHandlers` — línea 179.
- `onItemClick` — línea 182.
- `listItems` — línea 207.
- `showItems` — línea 217.
- `FbListenerOrdenEstado` — línea 262.
- `registerListener` — línea 270.
- `unregisterListener` — línea 278.
- `crearVenta` — línea 290.
- `datosOrden` — línea 300.
- `buildVenta` — línea 321.
- `cargaOrden` — línea 357.
- `existeCliente` — línea 442.
- `addItem` — línea 489.
- `addItemOld` — línea 595.
- `registroFirebase` — línea 692.
- `fbrsActivas` — línea 716.
- `onItemClick` — línea 742.
- `onClick` — línea 760.
- `fbocCuentas` — línea 772.
- `onItemClick` — línea 795.
- `onClick` — línea 812.
- `fboPagada` — línea 824.
- `crearAvisoPago` — línea 840.
- `mesaActiva` — línea 863.
- `ventaVacia` — línea 884.
- `datosCuenta` — línea 903.
- `cargaCliente` — línea 911.
- `cargaDatosCliente` — línea 919.
- `calibraPantalla` — línea 956.
- `pantallaHorizontal` — línea 968.
- `getURL` — línea 978.
- `menuVenta` — línea 998.
- `showMenuMesa` — línea 1019.
- `onItemClick` — línea 1033.
- `onClick` — línea 1071.
- `msgAskPagar` — línea 1083.
- `onClick` — línea 1091.
- `onClick` — línea 1101.
- `msgSync` — línea 1110.
- `onClick` — línea 1117.
- `msgAskReset` — línea 1126.
- `onClick` — línea 1134.
- `onClick` — línea 1145.
- `inputPropina` — línea 1154.
- `onClick` — línea 1167.
- `onClick` — línea 1178.
- `askPropina` — línea 1184.
- `onResume` — línea 1212.
- `onPause` — línea 1231.
- `onBackPressed` — línea 1238.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

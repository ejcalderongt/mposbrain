# MainActivity

Dominio: `sync-configuration`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/MainActivity.java:93`; hereda `PBase`.

## Layouts candidatos

- `activity_main` — `app/src/main/java/com/dtsgt/mpos/MainActivity.java:137`.
- `activity_main` — `app/src/main/java/com/dtsgt/mpos/MainActivity.java:140`.
- `activity_main` — `app/src/main/java/com/dtsgt/mpos/MainActivity.java:145`.
- `activity_main` — `app/src/main/java/com/dtsgt/mpos/MainActivity.java:182`.
- `activity_main2` — `app/src/main/java/com/dtsgt/mpos/MainActivity.java:185`.
- `activity_main` — `app/src/main/java/com/dtsgt/mpos/MainActivity.java:189`.

## Navegación candidata

- `Menu` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/MainActivity.java:390`; condiciones en catálogo.
- `WSRec` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/MainActivity.java:538`; condiciones en catálogo.
- `ConfigCaja` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/MainActivity.java:748`; condiciones en catálogo.
- `srvBase` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/MainActivity.java:966`; condiciones en catálogo.
- `ConfigCaja` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/MainActivity.java:1028`; condiciones en catálogo.
- `CuponEnvios` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/MainActivity.java:1600`; condiciones en catálogo.
- `ValidCorel` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/MainActivity.java:1961`; condiciones en catálogo.

## Estado global escrito

`CellCom`, `after_login`, `autocom`, `banderafindia`, `bloqueo_venta`, `caja`, `cajanom`, `clave`, `cliente_lealtad`, `codigo_pais`, `codigo_ruta`, `codigo_vendedor`, `debug`, `depparc`, `deviceId`, `devicename`, `devol`, `domicilio_notif`, `emp`, `empnom`, `felLlaveCertificacion`, `felUsuarioCertificacion`, `gpspx`, `gpspy`, `id_equipo`, `idmesero`, `impresora`, `incNoLectura`, `lotedf`, `modoadmin`, `modoinicial`, `nivel`, `nombre_mesero_sel`, `parVer`, `peMCent`, `pedido_dom_import`, `rol`, `rolmenu`, `ruta`, `rutanom`, `rutatipog`, `scrdim`, `sucur`, `tienda`, `tiendanit`, `tiendanom`, `umpeso`, `urlglob`, `usarpeso`, `vend`, `vendnom`, `vnivprec`, `wsurl`

## Tablas mencionadas estáticamente

`D_USUARIO_ASISTENCIA`, `PARAMS`, `P_EMPRESA`, `P_RUTA`, `P_SUCURSAL`, `P_VENDEDOR_SUCURSAL`, `VENDEDORES`

## Métodos

- `onCreate` — línea 129.
- `onConfigurationChanged` — línea 172.
- `grantPermissions` — línea 200.
- `startApplication` — línea 264.
- `onRequestPermissionsResult` — línea 333.
- `comMan` — línea 377.
- `gotoMenu` — línea 381.
- `doOrientation` — línea 409.
- `doLoginScreen` — línea 413.
- `doRegister` — línea 419.
- `doKey` — línea 432.
- `doFPTest` — línea 449.
- `doFELESA` — línea 454.
- `doFragTest` — línea 460.
- `setHandlers` — línea 465.
- `onItemClick` — línea 470.
- `onItemSelected` — línea 491.
- `onNothingSelected` — línea 505.
- `initSession` — línea 521.
- `processLogIn` — línea 680.
- `checkUser` — línea 687.
- `setRol` — línea 797.
- `logUser` — línea 834.
- `iniciaPantalla` — línea 865.
- `guardaPantalla` — línea 896.
- `iniciaDomicilio` — línea 915.
- `registerEventListener` — línea 930.
- `onDataChange` — línea 934.
- `onCancelled` — línea 945.
- `notifyMsg` — línea 957.
- `createID` — línea 994.
- `accesoAdmin` — línea 1004.
- `onClick` — línea 1024.
- `onClick` — línea 1042.
- `dbVacia` — línea 1055.
- `validaLicencia` — línea 1071.
- `androidid` — línea 1131.
- `getLocalBluetoothName` — línea 1152.
- `configBase` — línea 1163.
- `tieneTiendaCaja` — línea 1258.
- `llenaUsuarios` — línea 1287.
- `pantallaPortrait` — línea 1353.
- `pantallaHorizontal` — línea 1361.
- `horizscr` — línea 1392.
- `toasthoriz` — línea 1405.
- `ubicacion` — línea 1411.
- `onLocationChanged` — línea 1426.
- `onProviderDisabled` — línea 1430.
- `onProviderEnabled` — línea 1434.
- `onStatusChanged` — línea 1438.
- `dodwn` — línea 1468.
- `registraVersion` — línea 1487.
- `msgAskLic` — línea 1510.
- `onClick` — línea 1518.
- `showOrientMenu` — línea 1526.
- `copyexist` — línea 1563.
- `cbcopyexist` — línea 1577.
- `testButton` — línea 1586.
- `envioCupon` — línea 1597.
- `createCupon` — línea 1606.
- `createCuponOrig` — línea 1634.
- `sendgmail` — línea 1658.
- `sendgmail3` — línea 1697.
- `sendEmailGmail` — línea 1752.
- `showCustomDialog` — línea 1934.
- `testCorrel` — línea 1959.
- `test3x5` — línea 1968.
- `doDialog` — línea 1982.
- `PassDlg` — línea 1986.
- `onClick` — línea 1992.
- `onClick` — línea 2000.
- `ListDlg` — línea 2024.
- `onClick` — línea 2032.
- `onClick` — línea 2040.
- `onClick` — línea 2048.
- `onItemClick` — línea 2056.
- `ListDlgOld` — línea 2085.
- `onItemClick` — línea 2102.
- `ListDlgChk` — línea 2131.
- `onClick` — línea 2137.
- `onClick` — línea 2145.
- `onClick` — línea 2153.
- `dlgTemplate` — línea 2189.
- `onItemClick` — línea 2200.
- `onClick` — línea 2213.
- `onResume` — línea 2231.
- `onDestroy` — línea 2258.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

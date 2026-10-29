# CliDet

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CliDet.java:44`; hereda `PBase`.

## Layouts candidatos

- `activity_cli_det` — `app/src/main/java/com/dtsgt/mpos/CliDet.java:68`.

## Navegación candidata

- `Aprofam1` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliDet.java:454`; condiciones en catálogo.
- `Venta` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliDet.java:456`; condiciones en catálogo.
- `Cobro` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliDet.java:612`; condiciones en catálogo.
- `CliGPS` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliDet.java:723`; condiciones en catálogo.
- `com.whatsapp` (external_app_candidate) — `app/src/main/java/com/dtsgt/mpos/CliDet.java:740`; condiciones en catálogo.
- `DevolCli` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliDet.java:823`; condiciones en catálogo.

## Estado global escrito

`banderaCobro`, `clitipo`, `contrib`, `credito`, `devtipo`, `gDirCliente`, `gNITCliente`, `gNombreCliente`, `gpspass`, `media`, `nivel`, `percepcion`, `rutatipo`, `tiponcredito`, `validarCred`, `vcheque`, `vchequepost`, `vcredito`

## Tablas mencionadas estáticamente

`D_FACTURAF`, `P_CLIENTE`, `P_COREL`

## Métodos

- `onCreate` — línea 65.
- `onSaveInstanceState` — línea 139.
- `onRestoreInstanceState` — línea 149.
- `showVenta` — línea 162.
- `showPreventa` — línea 176.
- `showDespacho` — línea 190.
- `showCredit` — línea 206.
- `showDevol` — línea 220.
- `tomarFoto` — línea 234.
- `mostrarFachada` — línea 262.
- `onActivityResult` — línea 265.
- `setHandlers` — línea 294.
- `onCheckedChanged` — línea 299.
- `onCheckedChanged` — línea 311.
- `showData` — línea 335.
- `calcCredit` — línea 402.
- `getUsedCred` — línea 436.
- `initVenta` — línea 450.
- `validaVenta` — línea 464.
- `redimensionarImagen` — línea 532.
- `inputFachada` — línea 544.
- `onClick` — línea 566.
- `doVenta` — línea 583.
- `doPreventa` — línea 599.
- `doCredit` — línea 608.
- `VerificaCantidad` — línea 619.
- `runVenta` — línea 642.
- `showDir` — línea 646.
- `inputCliente` — línea 656.
- `onClick` — línea 688.
- `onClick` — línea 697.
- `ActualizarCliente` — línea 709.
- `setGPS` — línea 720.
- `sendSMS` — línea 730.
- `callPhone` — línea 761.
- `callWaze` — línea 785.
- `setDevType` — línea 820.
- `habilitaOpciones` — línea 831.
- `toastcent` — línea 858.
- `doExit` — línea 870.
- `msgAskGPSVenta` — línea 883.
- `onClick` — línea 893.
- `onClick` — línea 909.
- `msgAskExit` — línea 918.
- `onClick` — línea 927.
- `onClick` — línea 933.
- `msgAskTipoEstadoDev` — línea 945.
- `onClick` — línea 953.
- `onClick` — línea 959.
- `msgAskTipoDev` — línea 974.
- `onClick` — línea 1004.
- `onClick` — línea 1018.
- `msgAskVenta` — línea 1033.
- `onClick` — línea 1042.
- `msgAskEditCliente` — línea 1054.
- `onClick` — línea 1062.
- `onClick` — línea 1068.
- `onResume` — línea 1085.
- `onBackPressed` — línea 1121.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

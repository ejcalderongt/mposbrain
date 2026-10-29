# Clientes

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/Clientes.java:44`; hereda `PBase`.

## Layouts candidatos

- `activity_clientes` — `app/src/main/java/com/dtsgt/mpos/Clientes.java:74`.

## Navegación candidata

- `MantCli` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Clientes.java:142`; condiciones en catálogo.
- `com.dts.uubio.uusample` (external_app_candidate) — `app/src/main/java/com/dtsgt/mpos/Clientes.java:178`; condiciones en catálogo.
- `Venta` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Clientes.java:427`; condiciones en catálogo.

## Estado global escrito

`cliente`, `codigo_cliente`, `escaneo`, `gNITCliente`, `gNombreCliente`, `gcods`, `scancliente`

## Tablas mencionadas estáticamente

`D_CLINUEVO`, `D_FACTURA`, `FPRINT`, `P_CLIENTE`, `P_COREL`

## Métodos

- `onCreate` — línea 71.
- `dispatchKeyEvent` — línea 115.
- `applyFilter` — línea 126.
- `CliNuevo` — línea 137.
- `callFPScan` — línea 150.
- `setHandlers` — línea 201.
- `onItemClick` — línea 205.
- `onItemLongClick` — línea 228.
- `onItemSelected` — línea 251.
- `onNothingSelected` — línea 273.
- `onItemSelected` — línea 281.
- `onNothingSelected` — línea 286.
- `afterTextChanged` — línea 295.
- `beforeTextChanged` — línea 298.
- `onTextChanged` — línea 301.
- `onCheckedChanged` — línea 309.
- `listItems` — línea 324.
- `showCliente` — línea 421.
- `barcodeClient` — línea 435.
- `fprintClient` — línea 463.
- `validaVenta` — línea 521.
- `fillSpinners` — línea 583.
- `puedeborrarse` — línea 625.
- `puedeeditarse` — línea 646.
- `msgAskBor` — línea 663.
- `onClick` — línea 671.
- `onClick` — línea 677.
- `msgAskEdit` — línea 688.
- `onClick` — línea 695.
- `onClick` — línea 701.
- `borraCliNuevo` — línea 710.
- `loadAdd` — línea 727.
- `fotoCliente` — línea 740.
- `mostrarFotoCliente` — línea 766.
- `listFPrints` — línea 791.
- `nitnum` — línea 816.
- `onResume` — línea 838.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

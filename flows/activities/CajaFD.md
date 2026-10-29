# CajaFD

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CajaFD.java:37`; hereda `PBase`.

## Layouts candidatos

- `activity_caja_fd` — `app/src/main/java/com/dtsgt/mpos/CajaFD.java:72`.

## Navegación candidata

- `FELVerificacion` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaFD.java:195`; condiciones en catálogo.
- `FELVerificacion` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaFD.java:197`; condiciones en catálogo.
- `CuponVirEnvio` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaFD.java:211`; condiciones en catálogo.
- `CajaPagosPend` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaFD.java:238`; condiciones en catálogo.
- `CajaCierreX` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaFD.java:453`; condiciones en catálogo.
- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaFD.java:691`; condiciones en catálogo.
- `CajaCierreX` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaFD.java:1171`; condiciones en catálogo.
- `WSRec` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaFD.java:1201`; condiciones en catálogo.

## Estado global escrito

`FinMonto`, `autocom`, `corelZ`, `fact_sin_cert`, `fd_cajapagos`, `fd_hn_corf`, `fd_hn_cori`, `fd_hn_exen`, `fd_hn_grav`, `fd_hn_imp`, `felcorel`, `feluuid`, `fondoCaja`, `monto_final_ingresado`, `recibir_automatico`, `reportid`

## Tablas mencionadas estáticamente

`D_FACTURA`, `D_FACTURAHN`, `D_FACTURAP`, `P_CAJACIERRE`, `P_CAJAPAGOS`, `P_MEDIAPAGO`, `P_SUCURSAL`, `T_BARRA_BONIF`, `T_CAJACIERRE`, `T_CIERRE_CRED`

## Métodos

- `onCreate` — línea 66.
- `save` — línea 228.
- `doExit` — línea 232.
- `pendiente` — línea 236.
- `doFondoClick` — línea 241.
- `doEfectClick` — línea 245.
- `setHandlers` — línea 252.
- `onItemClick` — línea 264.
- `listItems` — línea 282.
- `cierreCaja` — línea 291.
- `procesaTransaccion` — línea 459.
- `transaccionCaja` — línea 480.
- `validaMontos` — línea 707.
- `diferenciaMontos` — línea 754.
- `actualizarFacturas` — línea 832.
- `factTotHonduras` — línea 920.
- `cierreCajaOrig` — línea 955.
- `msgAskExit` — línea 1186.
- `msgAskSend` — línea 1216.
- `msgAskCierre` — línea 1231.
- `msgAskCierreSeguro` — línea 1246.
- `msgAskCierreImpresion` — línea 1261.
- `inputValor` — línea 1275.
- `onClick` — línea 1282.
- `onClick` — línea 1289.
- `inputValorFondo` — línea 1311.
- `onClick` — línea 1318.
- `onClick` — línea 1325.
- `inputValorEfect` — línea 1339.
- `onClick` — línea 1346.
- `onClick` — línea 1354.
- `msgboxValidaMonto` — línea 1369.
- `onClick` — línea 1380.
- `onClick` — línea 1387.
- `cuentasPendientes` — línea 1412.
- `cbCuentasPendientes` — línea 1420.
- `validaFacturas` — línea 1438.
- `validaEnvioTarjetas` — línea 1465.
- `captcha` — línea 1476.
- `validaPendiente` — línea 1483.
- `writeCorelLog` — línea 1487.
- `validaFechaContrato` — línea 1496.
- `t_cajaadd` — línea 1525.
- `pendienteFEL` — línea 1550.
- `pendienteFELHoy` — línea 1576.
- `onResume` — línea 1594.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

# Caja

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/Caja.java:44`; hereda `PBase`.

## Layouts candidatos

- `activity_caja` — `app/src/main/java/com/dtsgt/mpos/Caja.java:78`.

## Navegación candidata

- `FELVerificacion` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Caja.java:221`; condiciones en catálogo.
- `FELVerificacion` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Caja.java:223`; condiciones en catálogo.
- `CajaPagosPend` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Caja.java:266`; condiciones en catálogo.
- `CierreX` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Caja.java:765`; condiciones en catálogo.
- `WSRec` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Caja.java:1033`; condiciones en catálogo.
- `CierreX` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Caja.java:1067`; condiciones en catálogo.
- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Caja.java:1072`; condiciones en catálogo.

## Estado global escrito

`FinMonto`, `autocom`, `corelZ`, `fact_sin_cert`, `fd_cajapagos`, `fd_hn_corf`, `fd_hn_cori`, `fd_hn_exen`, `fd_hn_grav`, `fd_hn_imp`, `felcorel`, `feluuid`, `fondoCaja`, `inicia_caja_primera_vez`, `inicio_caja_correcto`, `monto_final_ingresado`, `recibir_automatico`, `reportid`, `servidor_anio`

## Tablas mencionadas estáticamente

`D_FACTURA`, `D_FACTURAHN`, `D_FACTURAP`, `P_CAJACIERRE`, `P_CAJAPAGOS`, `P_MEDIAPAGO`, `P_SUCURSAL`, `T_BARRA_BONIF`, `T_CIERRE_CRED`, `T_LIC_ESTADO`

## Métodos

- `onCreate` — línea 75.
- `save` — línea 239.
- `doExit` — línea 260.
- `pendiente` — línea 264.
- `doFondoClick` — línea 269.
- `doEfectClick` — línea 273.
- `setHandlers` — línea 280.
- `onItemClick` — línea 292.
- `listItems` — línea 310.
- `guardar` — línea 319.
- `montoDif` — línea 379.
- `saveMontoIni` — línea 479.
- `Actualizar_Facturas_Sin_Corel_Cierre2` — línea 787.
- `validacionesInicio` — línea 897.
- `factTotHonduras` — línea 921.
- `checkDate` — línea 961.
- `dateCallback` — línea 976.
- `msgAskExit` — línea 1017.
- `msgAskCuentas` — línea 1047.
- `msgAskExit2` — línea 1055.
- `msgAskSend` — línea 1082.
- `msgAskFecha` — línea 1093.
- `msgAskFechaIni` — línea 1101.
- `msgAskNoFecha` — línea 1109.
- `msgAskFechaContinuar` — línea 1117.
- `msgText` — línea 1126.
- `inputValor` — línea 1134.
- `onClick` — línea 1141.
- `onClick` — línea 1148.
- `inputValorFondo` — línea 1170.
- `onClick` — línea 1177.
- `onClick` — línea 1184.
- `inputValorEfect` — línea 1198.
- `onClick` — línea 1205.
- `onClick` — línea 1213.
- `msgboxValidaMonto` — línea 1228.
- `onClick` — línea 1239.
- `onClick` — línea 1246.
- `validaFacturas` — línea 1310.
- `enviaAvizo` — línea 1337.
- `captcha` — línea 1390.
- `validaPendiente` — línea 1397.
- `writeCorelLog` — línea 1401.
- `validaFechaContrato` — línea 1410.
- `getEstadoLicencia` — línea 1439.
- `pendienteFEL` — línea 1463.
- `pendienteFELHoy` — línea 1489.
- `cuentasAbiertas` — línea 1503.
- `onResume` — línea 1527.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

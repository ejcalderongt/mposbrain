# CierreX

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CierreX.java:60`; hereda `PBase`.

## Layouts candidatos

- `activity_cierre_x` — `app/src/main/java/com/dtsgt/mpos/CierreX.java:97`.
- `activity_cierre_x_ver` — `app/src/main/java/com/dtsgt/mpos/CierreX.java:99`.

## Navegación candidata

- `WSEnv` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CierreX.java:1661`; condiciones en catálogo.
- `this.getPackageName` (external_app_candidate) — `app/src/main/java/com/dtsgt/mpos/CierreX.java:1816`; condiciones en catálogo.

## Estado global escrito

`QRCodeStr`, `autocom`

## Tablas mencionadas estáticamente

`D_CIERRE`, `D_FACTURA`, `D_FACTURAD`, `P_CAJACIERRE`, `P_CLIENTE`, `P_LINEA`, `P_MEDIAPAGO`, `P_PRODUCTO`, `P_SUCURSAL`, `T_BARRA_BONIF`, `T_CIERRE`, `VENDEDORES`

## Métodos

- `onCreate` — línea 89.
- `GeneratePrintCierre` — línea 167.
- `isValidEmail` — línea 268.
- `setHandlers` — línea 277.
- `fillItems` — línea 401.
- `reporteZ` — línea 690.
- `depositos` — línea 793.
- `getTXT` — línea 812.
- `GenerarCopiaReporte` — línea 845.
- `printDoc` — línea 874.
- `cuentasAbiertas` — línea 885.
- `msgAskOk` — línea 1646.
- `msgAskExit` — línea 1653.
- `msgAskReset` — línea 1671.
- `respaldoReporte` — línea 1682.
- `agregarReporte` — línea 1704.
- `writeCorelLog` — línea 1741.
- `EnviarCierre` — línea 1751.
- `checkPrintFile` — línea 1774.
- `restartApp` — línea 1813.
- `pantallaHorizontal` — línea 1828.
- `SetCorreoCliente` — línea 1838.
- `msgAsk` — línea 1947.
- `onResume` — línea 1966.
- `onBackPressed` — línea 1976.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

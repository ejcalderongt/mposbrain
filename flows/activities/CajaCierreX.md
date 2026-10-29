# CajaCierreX

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CajaCierreX.java:73`; hereda `PBase`.

## Layouts candidatos

- `activity_caja_cierre_x` — `app/src/main/java/com/dtsgt/mpos/CajaCierreX.java:111`.
- `activity_caja_cierre_x_ver` — `app/src/main/java/com/dtsgt/mpos/CajaCierreX.java:113`.

## Navegación candidata

- `this.getPackageName` (external_app_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaCierreX.java:1984`; condiciones en catálogo.

## Estado global escrito

`QRCodeStr`

## Tablas mencionadas estáticamente

`D_CIERRE`, `D_FACTURA`, `D_FACTURAD`, `P_CLIENTE`, `P_LINEA`, `P_MEDIAPAGO`, `P_PRODUCTO`, `P_SUCURSAL`, `T_BARRA_BONIF`, `T_CAJACIERRE`, `T_CIERRE`, `VENDEDORES`

## Métodos

- `onCreate` — línea 104.
- `onGen` — línea 189.
- `onExit` — línea 193.
- `setHandlers` — línea 203.
- `fillItems` — línea 331.
- `GeneratePrintCierre` — línea 449.
- `condicion1` — línea 549.
- `condicion2` — línea 571.
- `condicion3` — línea 586.
- `condicion4` — línea 603.
- `condicion5` — línea 624.
- `condicion6` — línea 639.
- `condicion7` — línea 652.
- `condicion8` — línea 666.
- `condicion9` — línea 682.
- `condicion10` — línea 697.
- `condicion11` — línea 713.
- `reporteZ` — línea 729.
- `depositos` — línea 821.
- `getTXT` — línea 840.
- `GenerarCopiaReporte` — línea 882.
- `crearArchivoPdf` — línea 910.
- `enviaPdfFireBase` — línea 940.
- `onSuccess` — línea 956.
- `run` — línea 959.
- `onFailure` — línea 971.
- `run` — línea 975.
- `printDoc` — línea 991.
- `createPdf` — línea 1006.
- `createPdfOld` — línea 1030.
- `msgAskOk` — línea 1790.
- `msgAskExit` — línea 1801.
- `msgAskReset` — línea 1825.
- `msgAsk` — línea 1836.
- `respaldoReporte` — línea 1855.
- `agregarReporte` — línea 1877.
- `writeCorelLog` — línea 1914.
- `EnviarCierre` — línea 1924.
- `checkPrintFile` — línea 1946.
- `restartApp` — línea 1981.
- `pantallaHorizontal` — línea 1994.
- `SetCorreoCliente` — línea 2004.
- `isValidEmail` — línea 2028.
- `onResume` — línea 2116.
- `onBackPressed` — línea 2126.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

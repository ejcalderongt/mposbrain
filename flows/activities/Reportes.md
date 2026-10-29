# Reportes

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/Reportes.java:46`; hereda `PBase`.

## Layouts candidatos

- `activity_reportes` — `app/src/main/java/com/dtsgt/mpos/Reportes.java:104`.
- `activity_reportes_ver` — `app/src/main/java/com/dtsgt/mpos/Reportes.java:106`.

## Navegación candidata

- `com.dts.epsonprint` (external_app_candidate) — `app/src/main/java/com/dtsgt/mpos/Reportes.java:212`; condiciones en catálogo.

## Estado global escrito

`QRCodeStr`, `reportid`, `validimp`

## Tablas mencionadas estáticamente

`D_FACTURA`, `D_FACTURAC`, `D_FACTURACOR`, `D_FACTURAD`, `D_FACTURAR`, `D_NOTAENVIO`, `D_NOTAENVIOD`, `D_ORDEN_STAT`, `P_CAJAPAGOS`, `P_CLIENTE`, `P_CONCEPTOPAGO`, `P_CORTESIA`, `P_LINEA`, `P_MEDIAPAGO`, `P_PRODUCTO`, `VENDEDORES`

## Métodos

- `onCreate` — línea 100.
- `run` — línea 172.
- `GeneratePrint` — línea 187.
- `printDoc` — línea 202.
- `printEpson` — línea 210.
- `setHandlers` — línea 224.
- `onItemClick` — línea 228.
- `onCheckedChanged` — línea 295.
- `onKey` — línea 309.
- `listItems` — línea 328.
- `AskReport` — línea 448.
- `getTXT` — línea 503.
- `fillItems` — línea 528.
- `obtenerFecha` — línea 831.
- `onDateSet` — línea 836.
- `getFechaAct` — línea 877.
- `clear` — línea 1587.
- `showDateDialog1` — línea 1592.
- `showDateDialog2` — línea 1602.
- `pantallaHorizontal` — línea 1612.
- `onResume` — línea 1626.
- `onPause` — línea 1635.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

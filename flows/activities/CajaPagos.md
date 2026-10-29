# CajaPagos

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CajaPagos.java:34`; hereda `PBase`.

## Layouts candidatos

- `activity_caja_pagos` — `app/src/main/java/com/dtsgt/mpos/CajaPagos.java:70`.

## Navegación candidata

- `Lista` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaPagos.java:112`; condiciones en catálogo.

## Estado global escrito

`dialogr`, `mantid`

## Tablas mencionadas estáticamente

`P_CONCEPTOPAGO`, `P_PROVEEDOR`, `P_PROVEEDOR_SUCURSAL`

## Métodos

- `onCreate` — línea 65.
- `run` — línea 88.
- `doSave` — línea 105.
- `doProveedor` — línea 109.
- `doDate` — línea 115.
- `doExit` — línea 119.
- `setHandlers` — línea 123.
- `onItemSelected` — línea 126.
- `onNothingSelected` — línea 142.
- `onItemSelected` — línea 150.
- `onNothingSelected` — línea 171.
- `save` — línea 184.
- `Item` — línea 235.
- `obtenerFecha` — línea 345.
- `onDateSet` — línea 349.
- `dialogswitch` — línea 377.
- `msgAskExit` — línea 390.
- `onClick` — línea 395.
- `onClick` — línea 401.
- `fillSpinner` — línea 412.
- `fillSpinner2` — línea 463.
- `getdate` — línea 516.
- `GeneratePrint` — línea 537.
- `onResume` — línea 553.
- `onBackPressed` — línea 569.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

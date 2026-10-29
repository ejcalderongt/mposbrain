# TallaColorExist

Dominio: `inventory`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/TallaColorExist.java:29`; hereda `PBase`.

## Layouts candidatos

- `activity_talla_color_exist` — `app/src/main/java/com/dtsgt/mpos/TallaColorExist.java:57`.

## Navegación candidata

- `TallaColorSucursal` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/TallaColorExist.java:110`; condiciones en catálogo.
- `TallaColorSucursal` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/TallaColorExist.java:427`; condiciones en catálogo.

## Estado global escrito

`tc_prodnom`, `tc_unidad`

## Tablas mencionadas estáticamente

`T_VENTA_TALLA_STOCK`

## Métodos

- `onCreate` — línea 53.
- `doExit` — línea 89.
- `setHandlers` — línea 93.
- `onItemClick` — línea 96.
- `initSession` — línea 124.
- `listItems` — línea 143.
- `compare` — línea 164.
- `cbLlenaExistencias` — línea 181.
- `listaDetalle` — línea 235.
- `listaSucursales` — línea 283.
- `proximaSucursal` — línea 296.
- `run` — línea 301.
- `procesaSucursal` — línea 317.
- `cbProcesaSucursal` — línea 332.
- `completaSucursales` — línea 382.
- `showMenu` — línea 411.
- `nombreColor` — línea 448.
- `rightPad` — línea 461.
- `setIdle` — línea 472.
- `onResume` — línea 480.
- `onBackPressed` — línea 494.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

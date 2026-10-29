# InvTransAlm

Dominio: `inventory`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/InvTransAlm.java:32`; hereda `PBase`.

## Layouts candidatos

- `activity_inv_trans_alm` — `app/src/main/java/com/dtsgt/mpos/InvTransAlm.java:65`.

## Navegación candidata

- `InvTransAlmDet` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/InvTransAlm.java:829`; condiciones en catálogo.

## Estado global escrito

`dialogr`, `idtrasalmacen`

## Tablas mencionadas estáticamente

`D_MOVD_ALMACEN`, `D_MOV_ALMACEN`, `D_TRASLADO_ALMACEN`, `P_ALMACEN`, `T_ALMACEN`, `T_MOVD_ALMACEN`, `T_MOV_ALMACEN`

## Métodos

- `onCreate` — línea 61.
- `onAdd` — línea 107.
- `doAlmOrig` — línea 116.
- `doAlmDest` — línea 121.
- `showDateDialog1` — línea 126.
- `showDateDialog2` — línea 135.
- `setHandlers` — línea 144.
- `onItemClick` — línea 147.
- `listItems` — línea 167.
- `almTrans` — línea 199.
- `cbAlmTrans` — línea 214.
- `listaTras` — línea 268.
- `cbTrasLista` — línea 282.
- `mostrarListaTras` — línea 315.
- `recibirEncTras` — línea 342.
- `cbTrasEnc` — línea 358.
- `recibirDetTras` — línea 412.
- `cbTrasDet` — línea 423.
- `cambiaEstadoRemoto` — línea 480.
- `cbCamEstado` — línea 495.
- `anularTraslado` — línea 507.
- `cbAnulacion` — línea 522.
- `impresion` — línea 538.
- `impresionEncabezado` — línea 562.
- `impresionDetalle` — línea 608.
- `nombreOperador` — línea 630.
- `listaAlmacenes` — línea 644.
- `onItemClick` — línea 660.
- `onClick` — línea 684.
- `nombreAlmacen` — línea 696.
- `nombreEstado` — línea 705.
- `obtenerFecha` — línea 724.
- `onDateSet` — línea 739.
- `setFechaAct` — línea 772.
- `cancel` — línea 790.
- `dialogswitch` — línea 801.
- `menuItem` — línea 816.
- `onResume` — línea 851.
- `onBackPressed` — línea 871.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

# DomPedidos

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/DomPedidos.java:32`; hereda `PBase`.

## Layouts candidatos

- `activity_pedidos_dom` — `app/src/main/java/com/dtsgt/mpos/DomPedidos.java:65`.

## Navegación candidata

- `DomImport` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DomPedidos.java:101`; condiciones en catálogo.
- `DomPedComp` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DomPedidos.java:106`; condiciones en catálogo.
- `DomDetalle` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DomPedidos.java:128`; condiciones en catálogo.
- `DomEntrega` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DomPedidos.java:232`; condiciones en catálogo.
- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DomPedidos.java:264`; condiciones en catálogo.

## Estado global escrito

`cli_depto`, `cli_muni`, `codigo_cliente`, `dialogr`, `dom_det_cod`, `dom_est_val`, `gCorreoCliente`, `gDirCliente`, `gNITCliente`, `gNITcf`, `gNombreCliente`, `ped_dom_cambio`, `ped_dom_cliente`, `ped_dom_corel`, `ped_dom_dir`, `ped_dom_monto`, `ped_dom_orden`, `ped_dom_tel`, `ped_dom_texto`, `pedido_dom_import`, `ventalock`

## Tablas mencionadas estáticamente

`D_DOMICILIO_ENC`, `T_COMBO`, `T_VENTA`

## Métodos

- `onCreate` — línea 59.
- `doAdd` — línea 100.
- `doMenu` — línea 104.
- `doExit` — línea 109.
- `setHandlers` — línea 113.
- `onItemClick` — línea 116.
- `listItems` — línea 141.
- `calculaTotales` — línea 187.
- `aplicarEstado` — línea 216.
- `enviaEstado` — línea 241.
- `crearVenta` — línea 278.
- `cargaCliente` — línea 360.
- `initTimer` — línea 392.
- `run` — línea 396.
- `run` — línea 398.
- `cancelTimer` — línea 407.
- `processTimer` — línea 413.
- `dialogswitch` — línea 448.
- `onResume` — línea 464.
- `onPause` — línea 491.
- `onStart` — línea 497.
- `onStop` — línea 504.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

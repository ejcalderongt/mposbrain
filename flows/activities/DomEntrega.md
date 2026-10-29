# DomEntrega

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/DomEntrega.java:31`; hereda `PBase`.

## Layouts candidatos

- `activity_dom_entrega` — `app/src/main/java/com/dtsgt/mpos/DomEntrega.java:62`.

## Navegación candidata

- `DomRepartidor` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DomEntrega.java:93`; condiciones en catálogo.
- `DomPedComp` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DomEntrega.java:98`; condiciones en catálogo.
- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DomEntrega.java:317`; condiciones en catálogo.
- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DomEntrega.java:337`; condiciones en catálogo.
- `DomRepartidor` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DomEntrega.java:431`; condiciones en catálogo.
- `DomPago` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DomEntrega.java:436`; condiciones en catálogo.

## Estado global escrito

`dialogr`, `dom_det_cod`, `dom_est_val`, `ped_dom_orden`, `repartidor_codigo`, `repartidor_select`

## Tablas mencionadas estáticamente

`D_DOMICILIO_ENC`, `D_DOMICILIO_ENTREGA`, `P_SUCURSAL`

## Métodos

- `onCreate` — línea 58.
- `doAdd` — línea 91.
- `doMenu` — línea 96.
- `doExit` — línea 101.
- `setHandlers` — línea 105.
- `onItemClick` — línea 108.
- `listItems` — línea 134.
- `calculaTotales` — línea 195.
- `asignaRepartidor` — línea 217.
- `aplicarEstado` — línea 238.
- `enviaEstado` — línea 257.
- `completarOrden` — línea 285.
- `enviaEstadoCompleto` — línea 294.
- `cantidadOrdenes` — línea 329.
- `initTimer` — línea 351.
- `run` — línea 355.
- `run` — línea 357.
- `cancelTimer` — línea 366.
- `processTimer` — línea 372.
- `dialogswitch` — línea 399.
- `showItemMenu` — línea 411.
- `onItemClick` — línea 423.
- `onClick` — línea 453.
- `onResume` — línea 470.
- `onPause` — línea 502.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

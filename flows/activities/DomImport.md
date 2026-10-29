# DomImport

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/DomImport.java:25`; hereda `PBase`.

## Layouts candidatos

- `activity_dom_import` — `app/src/main/java/com/dtsgt/mpos/DomImport.java:52`.

## Navegación candidata

- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DomImport.java:328`; condiciones en catálogo.

## Estado global escrito

No detectado.

## Tablas mencionadas estáticamente

`D_DOMICILIO_COMBO`, `D_DOMICILIO_DET`, `D_DOMICILIO_ENC`, `P_ORDEN_NUMERO`, `P_SUCURSAL`

## Métodos

- `onCreate` — línea 48.
- `listItems` — línea 87.
- `cantPendientes` — línea 95.
- `procesaPedido` — línea 117.
- `run` — línea 125.
- `cargaEncabezado` — línea 136.
- `llenaEncabezado` — línea 145.
- `cargaDetalle` — línea 162.
- `cargaCombos` — línea 172.
- `guardaPedido` — línea 182.
- `proximoPedido` — línea 232.
- `msgexit` — línea 245.
- `onClick` — línea 254.
- `finpedidos` — línea 269.
- `finok` — línea 283.
- `finerr` — línea 288.
- `numeroOrdenLocal` — línea 293.
- `cantidadOrdenes` — línea 320.
- `onResume` — línea 342.
- `onBackPressed` — línea 355.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

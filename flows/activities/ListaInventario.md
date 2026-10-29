# ListaInventario

Dominio: `inventory`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:43`; hereda `PBase`.

## Layouts candidatos

- `activity_lista_inventario` — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:81`.

## Navegación candidata

- `srvInventConfirm` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:140`; condiciones en catálogo.
- `Lista` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:217`; condiciones en catálogo.
- `InvAjuste` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:221`; condiciones en catálogo.
- `InvAjuste` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:227`; condiciones en catálogo.
- `Lista` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:234`; condiciones en catálogo.
- `InvAjuste` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:238`; condiciones en catálogo.
- `InvEgreso` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:243`; condiciones en catálogo.
- `InvEgreso` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:248`; condiciones en catálogo.
- `InvTomInventario` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:256`; condiciones en catálogo.
- `InvTomInventario` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:290`; condiciones en catálogo.
- `InvVista` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:585`; condiciones en catálogo.
- `InvRecep` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:862`; condiciones en catálogo.
- `InvRecep` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:910`; condiciones en catálogo.
- `InvTomInventario` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:935`; condiciones en catálogo.
- `InvRecep` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:983`; condiciones en catálogo.
- `InvRecep` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventario.java:1131`; condiciones en catálogo.

## Estado global escrito

`closeDevBod`, `codigo_proveedor`, `corelmov`, `docnumMov`, `idalm`, `idalmpred`, `idmov`, `imp_inventario`, `invregular`, `listaedit`, `mantid`, `nom_alm`, `nombre_proveedor`, `tipo`

## Tablas mencionadas estáticamente

`D_COMPRA_LOCAL`, `D_MOV`, `D_MOVD`, `D_MOV_ALMACEN`

## Métodos

- `onCreate` — línea 76.
- `run` — línea 124.
- `confirmaInventario` — línea 138.
- `nuevo` — línea 149.
- `doAlmacenes` — línea 267.
- `setHandlers` — línea 271.
- `onItemClick` — línea 275.
- `onItemLongClick` — línea 314.
- `listItems` — línea 347.
- `existeInventarioPendiente` — línea 538.
- `cargaDocumento` — línea 577.
- `showDateDialog1` — línea 594.
- `showDateDialog2` — línea 603.
- `obtenerFecha` — línea 612.
- `onDateSet` — línea 615.
- `setFechaAct` — línea 667.
- `generarImpresion` — línea 691.
- `impresionEncabezado` — línea 735.
- `impresionDetalle` — línea 812.
- `msgAskResume` — línea 853.
- `onClick` — línea 860.
- `onClick` — línea 867.
- `onClick` — línea 873.
- `msgAskDelete` — línea 881.
- `onClick` — línea 888.
- `onClick` — línea 894.
- `msgAskImprimir` — línea 901.
- `onClick` — línea 908.
- `onClick` — línea 915.
- `onClick` — línea 919.
- `mostrarDlgInventarioPendiente` — línea 928.
- `validaInicial` — línea 948.
- `abrirInicial` — línea 975.
- `borrarIngreso` — línea 989.
- `nombreAlmacen` — línea 1006.
- `nombreProveedor` — línea 1019.
- `nombreOperador` — línea 1029.
- `tieneAlmacenes` — línea 1039.
- `listaAlmacenes` — línea 1066.
- `onItemClick` — línea 1080.
- `onClick` — línea 1098.
- `onResume` — línea 1115.
- `run` — línea 1145.
- `onBackPressed` — línea 1155.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

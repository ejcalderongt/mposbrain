# ListaCompras

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/ListaCompras.java:34`; hereda `PBase`.

## Layouts candidatos

- `activity_lista_compras` — `app/src/main/java/com/dtsgt/mpos/ListaCompras.java:67`.

## Navegación candidata

- `Lista` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaCompras.java:116`; condiciones en catálogo.
- `InvAjuste` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaCompras.java:120`; condiciones en catálogo.
- `InvAjuste` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaCompras.java:126`; condiciones en catálogo.
- `Lista` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaCompras.java:133`; condiciones en catálogo.
- `InvAjuste` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaCompras.java:137`; condiciones en catálogo.
- `InvEgreso` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaCompras.java:142`; condiciones en catálogo.
- `InvEgreso` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaCompras.java:147`; condiciones en catálogo.
- `InvVista` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaCompras.java:366`; condiciones en catálogo.
- `InvRecep` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaCompras.java:718`; condiciones en catálogo.
- `InvRecep` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaCompras.java:816`; condiciones en catálogo.

## Estado global escrito

`closeDevBod`, `codigo_proveedor`, `corelmov`, `idmov`, `invregular`, `listaedit`, `mantid`, `nom_est`, `nombre_proveedor`, `tipo`

## Tablas mencionadas estáticamente

`D_COMPRA_LOCAL`, `D_MOV`, `D_MOVD`, `D_MOV_ALMACEN`

## Métodos

- `onCreate` — línea 64.
- `nuevo` — línea 97.
- `doAlmacenes` — línea 162.
- `setHandlers` — línea 166.
- `onItemClick` — línea 170.
- `onItemLongClick` — línea 199.
- `listItems` — línea 229.
- `cargaDocumento` — línea 358.
- `showDateDialog1` — línea 376.
- `showDateDialog2` — línea 386.
- `obtenerFecha` — línea 396.
- `onDateSet` — línea 399.
- `setFechaAct` — línea 453.
- `generarImpresion` — línea 478.
- `impresionEncabezado` — línea 520.
- `impresionDetalle` — línea 577.
- `msgAskResume` — línea 618.
- `onClick` — línea 625.
- `onClick` — línea 631.
- `msgAskDelete` — línea 639.
- `onClick` — línea 646.
- `onClick` — línea 652.
- `msgAskImprimir` — línea 659.
- `onClick` — línea 666.
- `onClick` — línea 670.
- `validaInicial` — línea 683.
- `abrirInicial` — línea 710.
- `borrarIngreso` — línea 725.
- `nombreProveedor` — línea 742.
- `nombreOperador` — línea 752.
- `listaEstados` — línea 762.
- `onItemClick` — línea 773.
- `onClick` — línea 789.
- `onResume` — línea 806.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

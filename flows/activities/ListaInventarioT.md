# ListaInventarioT

Dominio: `inventory`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/ListaInventarioT.java:42`; hereda `PBase`.

## Layouts candidatos

- `activity_lista_inventario_t` — `app/src/main/java/com/dtsgt/mpos/ListaInventarioT.java:78`.

## Navegación candidata

- `srvInventConfirm` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventarioT.java:147`; condiciones en catálogo.
- `InvTrans` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventarioT.java:178`; condiciones en catálogo.
- `InvVista` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventarioT.java:407`; condiciones en catálogo.
- `InvRecep` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventarioT.java:687`; condiciones en catálogo.
- `InvRecep` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventarioT.java:735`; condiciones en catálogo.
- `InvRecep` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaInventarioT.java:765`; condiciones en catálogo.

## Estado global escrito

`codigo_proveedor`, `corelmov`, `idalm`, `idalm2`, `idalmpred`, `idmov`, `invregular`, `nom_alm`, `nom_alm2`, `nombre_proveedor`

## Tablas mencionadas estáticamente

`D_COMPRA_LOCAL`, `D_MOV`, `D_MOVD`, `D_MOV_ALMACEN`

## Métodos

- `onCreate` — línea 75.
- `run` — línea 121.
- `run` — línea 133.
- `confirmaInventario` — línea 145.
- `nuevo` — línea 156.
- `doAlmacenes1` — línea 187.
- `doAlmacenes2` — línea 191.
- `setHandlers` — línea 197.
- `onItemClick` — línea 201.
- `onItemLongClick` — línea 230.
- `listItems` — línea 264.
- `cargaDocumento` — línea 399.
- `showDateDialog1` — línea 417.
- `showDateDialog2` — línea 427.
- `obtenerFecha` — línea 437.
- `onDateSet` — línea 440.
- `setFechaAct` — línea 494.
- `generarImpresion` — línea 519.
- `impresionEncabezado` — línea 561.
- `impresionDetalle` — línea 637.
- `msgAskResume` — línea 678.
- `onClick` — línea 685.
- `onClick` — línea 692.
- `onClick` — línea 698.
- `msgAskDelete` — línea 706.
- `onClick` — línea 713.
- `onClick` — línea 719.
- `msgAskImprimir` — línea 726.
- `onClick` — línea 733.
- `onClick` — línea 740.
- `onClick` — línea 744.
- `abrirInicial` — línea 757.
- `borrarIngreso` — línea 772.
- `listaAlmacenes1` — línea 789.
- `onItemClick` — línea 804.
- `onClick` — línea 817.
- `listaAlmacenes2` — línea 830.
- `onItemClick` — línea 846.
- `onClick` — línea 859.
- `nombreAlmacen` — línea 873.
- `nombreProveedor` — línea 882.
- `nombreOperador` — línea 892.
- `tieneAlmacenes` — línea 902.
- `onResume` — línea 929.
- `onBackPressed` — línea 942.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

# ResMesero

Dominio: `restaurant`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/ResMesero.java:55`; hereda `PBase`.

## Layouts candidatos

- `activity_res_mesero` — `app/src/main/java/com/dtsgt/mpos/ResMesero.java:105`.

## Navegación candidata

- `Nowifi` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ResMesero.java:196`; condiciones en catálogo.
- `Barriles` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ResMesero.java:201`; condiciones en catálogo.
- `Orden` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ResMesero.java:632`; condiciones en catálogo.
- `Comensales` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ResMesero.java:652`; condiciones en catálogo.
- `srvOrdenEnvio` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ResMesero.java:893`; condiciones en catálogo.

## Estado global escrito

`cerrarmesero`, `cliposflag`, `exitflag`, `idorden`, `mesa_alias`, `mesa_area`, `mesa_codigo`, `mesa_grupo`, `mesa_vend`, `mesacodigo`, `mesanom`, `mesero_venta`, `nueva_mesa`, `salaid`, `timeout`, `ventalock`, `wsurl`

## Tablas mencionadas estáticamente

`D_ORDEN_COREL`, `P_MESERO_GRUPO`, `P_RES_SESION`, `P_RES_SESION_ID_COR`, `P_RES_TURNO`, `T_ORDENCOM`

## Métodos

- `onCreate` — línea 100.
- `doGrupo` — línea 187.
- `doComp` — línea 191.
- `doSincon` — línea 195.
- `doBarril` — línea 199.
- `doExit` — línea 207.
- `setHandlers` — línea 215.
- `onItemClick` — línea 218.
- `onItemLongClick` — línea 249.
- `listItems` — línea 270.
- `fboeList` — línea 280.
- `showItems` — línea 293.
- `FbResSesionList` — línea 379.
- `tienePrecuenta` — línea 421.
- `abrirOrden` — línea 436.
- `abrirOrdenMesa` — línea 445.
- `addOrden` — línea 491.
- `listMesa` — línea 568.
- `onItemClick` — línea 581.
- `validaMesaAbierta` — línea 599.
- `validaMesaComensales` — línea 608.
- `FbMesaAbierta` — línea 617.
- `FbMesaComensales` — línea 638.
- `desbloquoMesa` — línea 658.
- `FbListenerResSesion` — línea 680.
- `procesaOrdenes` — línea 688.
- `confirmaOrdenes` — línea 753.
- `unregisterListener` — línea 761.
- `agregaOrden` — línea 773.
- `PutCorelCallback` — línea 789.
- `GetCorelCallback` — línea 803.
- `validaCompleto` — línea 840.
- `cerrarCuentas` — línea 863.
- `envioMesa` — línea 882.
- `estadoMesa` — línea 899.
- `mesaActiva` — línea 917.
- `aplicaNombreMesa` — línea 931.
- `cargaConfig` — línea 952.
- `setGrupo` — línea 980.
- `calibraPantalla` — línea 1008.
- `cantidadComensales` — línea 1022.
- `pantallaHorizontal` — línea 1033.
- `getURL` — línea 1043.
- `aliasMesa` — línea 1069.
- `borraNombreMesa` — línea 1082.
- `showGrupoMenu` — línea 1099.
- `onItemClick` — línea 1124.
- `showGrupoChecks` — línea 1153.
- `onClick` — línea 1171.
- `msgAskExit` — línea 1218.
- `onClick` — línea 1226.
- `onClick` — línea 1233.
- `opcionesMesa` — línea 1242.
- `onItemClick` — línea 1251.
- `onClick` — línea 1266.
- `ingresaNombreMesa` — línea 1279.
- `onClick` — línea 1291.
- `onClick` — línea 1316.
- `msgBoxWifi` — línea 1322.
- `onClick` — línea 1329.
- `msgAskMesa` — línea 1340.
- `onClick` — línea 1348.
- `onClick` — línea 1354.
- `msgdebloq` — línea 1363.
- `onClick` — línea 1371.
- `msgSync` — línea 1380.
- `onClick` — línea 1387.
- `msgAskMesaAbrir` — línea 1396.
- `onClick` — línea 1404.
- `onClick` — línea 1410.
- `validaSupervisor` — línea 1419.
- `validaSupervisorMesa` — línea 1462.
- `onResume` — línea 1509.
- `onPause` — línea 1551.
- `onBackPressed` — línea 1557.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

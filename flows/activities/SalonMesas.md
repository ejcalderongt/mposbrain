# SalonMesas

Dominio: `restaurant`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/SalonMesas.java:64`; hereda `PBase`.

## Layouts candidatos

- `activity_salon_mesas` — `app/src/main/java/com/dtsgt/mpos/SalonMesas.java:117`.

## Navegación candidata

- `Nowifi` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/SalonMesas.java:205`; condiciones en catálogo.
- `SalonOrden` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/SalonMesas.java:645`; condiciones en catálogo.
- `Comensales` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/SalonMesas.java:669`; condiciones en catálogo.
- `srvOrdenEnvio` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/SalonMesas.java:920`; condiciones en catálogo.

## Estado global escrito

`cerrarmesero`, `cliposflag`, `exitflag`, `idorden`, `mesa_alias`, `mesa_area`, `mesa_codigo`, `mesa_grupo`, `mesa_vend`, `mesacodigo`, `mesanom`, `mesero_venta`, `nueva_mesa`, `salaid`, `selcita_nombre`, `timeout`, `ventalock`, `wsurl`

## Tablas mencionadas estáticamente

`D_ORDEN_COREL`, `P_MESERO_GRUPO`, `P_PRODUCTO`, `P_RES_SESION`, `P_RES_SESION_ID_COR`, `P_RES_TURNO`, `T_ORDENCOM`

## Métodos

- `onCreate` — línea 110.
- `doCalendar` — línea 188.
- `doGrupo` — línea 196.
- `doComp` — línea 200.
- `doSincon` — línea 204.
- `doExit` — línea 208.
- `setHandlers` — línea 220.
- `onItemClick` — línea 223.
- `onItemLongClick` — línea 243.
- `listItems` — línea 264.
- `listNames` — línea 276.
- `fboctList` — línea 285.
- `showItems` — línea 299.
- `FbResSesionList` — línea 385.
- `tienePrecuenta` — línea 434.
- `abrirOrden` — línea 449.
- `abrirOrdenMesa` — línea 458.
- `addOrden` — línea 504.
- `listMesa` — línea 581.
- `onItemClick` — línea 594.
- `validaMesaAbierta` — línea 612.
- `validaMesaComensales` — línea 621.
- `FbMesaAbierta` — línea 630.
- `FbMesaComensales` — línea 651.
- `mesaTieneVendedor` — línea 677.
- `desbloquoMesa` — línea 685.
- `FbListenerResSesion` — línea 707.
- `procesaOrdenes` — línea 715.
- `confirmaOrdenes` — línea 780.
- `unregisterListener` — línea 788.
- `agregaOrden` — línea 800.
- `PutCorelCallback` — línea 816.
- `GetCorelCallback` — línea 830.
- `validaCompleto` — línea 867.
- `cerrarCuentas` — línea 890.
- `envioMesa` — línea 909.
- `estadoMesa` — línea 926.
- `calendarLista` — línea 944.
- `cbCalendarLista` — línea 954.
- `mostrarCalendarLista` — línea 977.
- `onItemClick` — línea 988.
- `showGrupoMenu` — línea 1008.
- `onItemClick` — línea 1033.
- `showGrupoChecks` — línea 1062.
- `onClick` — línea 1080.
- `msgAskExit` — línea 1127.
- `onClick` — línea 1135.
- `onClick` — línea 1142.
- `showListAsesor` — línea 1151.
- `onItemClick` — línea 1166.
- `msgdebloq` — línea 1188.
- `onClick` — línea 1196.
- `msgSync` — línea 1205.
- `onClick` — línea 1212.
- `validaSupervisor` — línea 1221.
- `mesaActiva` — línea 1268.
- `aplicaNombreMesa` — línea 1282.
- `cargaConfig` — línea 1303.
- `setGrupo` — línea 1335.
- `calibraPantalla` — línea 1366.
- `pantallaHorizontal` — línea 1373.
- `getURL` — línea 1383.
- `aliasMesa` — línea 1409.
- `borraNombreMesa` — línea 1422.
- `nombreSession` — línea 1435.
- `horaSession` — línea 1449.
- `horaMinSession` — línea 1463.
- `vendedorSession` — línea 1485.
- `prodNombre` — línea 1499.
- `onResume` — línea 1520.
- `onPause` — línea 1556.
- `onBackPressed` — línea 1562.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

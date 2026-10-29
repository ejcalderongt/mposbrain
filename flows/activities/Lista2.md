# Lista2

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mant/Lista2.java:24`; hereda `PBase`.

## Layouts candidatos

- `activity_lista2` — `app/src/main/java/com/dtsgt/mant/Lista2.java:41`.

## Navegación candidata

- `MantBanco` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista2.java:347`; condiciones en catálogo.
- `MantCli` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista2.java:349`; condiciones en catálogo.
- `MantEmpresa` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista2.java:351`; condiciones en catálogo.
- `MantFamilia` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista2.java:353`; condiciones en catálogo.
- `MantMediaPago` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista2.java:355`; condiciones en catálogo.
- `MantImpuesto` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista2.java:357`; condiciones en catálogo.
- `MantMoneda` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista2.java:359`; condiciones en catálogo.
- `MantProducto` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista2.java:361`; condiciones en catálogo.
- `MantProveedor` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista2.java:363`; condiciones en catálogo.
- `MantVendedores` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista2.java:365`; condiciones en catálogo.
- `MantTienda` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista2.java:367`; condiciones en catálogo.
- `MantCaja` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista2.java:369`; condiciones en catálogo.
- `MantNivelPrecio` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista2.java:371`; condiciones en catálogo.
- `MantDescuento` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista2.java:373`; condiciones en catálogo.

## Estado global escrito

`banco`, `disc`, `gcods`, `listaedit`, `pickcode`, `pickname`

## Tablas mencionadas estáticamente

`P_BANCO`, `P_CLIENTE`, `P_DESCUENTO`, `P_EMPRESA`, `P_IMPUESTO`, `P_LINEA`, `P_MEDIAPAGO`, `P_MONEDA`, `P_NIVELPRECIO`, `P_PRODOPC`, `P_PRODUCTO`, `P_PROVEEDOR`, `P_RUTA`, `P_SUCURSAL`, `VENDEDORES`

## Métodos

- `onCreate` — línea 38.
- `doAdd` — línea 65.
- `doClear` — línea 70.
- `doExit` — línea 74.
- `setHandlers` — línea 78.
- `onItemClick` — línea 81.
- `onCheckedChanged` — línea 103.
- `afterTextChanged` — línea 111.
- `beforeTextChanged` — línea 113.
- `onTextChanged` — línea 115.
- `listItems` — línea 126.
- `setTableSQL` — línea 165.
- `setMantID` — línea 299.
- `abrirMant` — línea 342.
- `onResume` — línea 388.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

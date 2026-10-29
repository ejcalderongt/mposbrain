# Lista

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mant/Lista.java:26`; hereda `PBase`.

## Layouts candidatos

- `activity_lista` — `app/src/main/java/com/dtsgt/mant/Lista.java:45`.

## Navegación candidata

- `MantBanco` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:500`; condiciones en catálogo.
- `MantCli` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:502`; condiciones en catálogo.
- `MantEmpresa` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:504`; condiciones en catálogo.
- `MantFamilia` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:506`; condiciones en catálogo.
- `MantMediaPago` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:508`; condiciones en catálogo.
- `MantImpuesto` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:510`; condiciones en catálogo.
- `MantMoneda` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:512`; condiciones en catálogo.
- `MantProducto` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:514`; condiciones en catálogo.
- `MantProveedor` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:516`; condiciones en catálogo.
- `MantVendedores` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:518`; condiciones en catálogo.
- `MantTienda` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:520`; condiciones en catálogo.
- `MantCaja` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:522`; condiciones en catálogo.
- `MantNivelPrecio` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:524`; condiciones en catálogo.
- `MantDescuento` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:526`; condiciones en catálogo.
- `MantConceptoPago` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:530`; condiciones en catálogo.
- `MantMotivoAjuste` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:532`; condiciones en catálogo.
- `MantResSala` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:534`; condiciones en catálogo.
- `MantResMesa` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:536`; condiciones en catálogo.
- `MantResGrupo` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:538`; condiciones en catálogo.
- `MantImpresora` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:540`; condiciones en catálogo.
- `MantEstacion` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:542`; condiciones en catálogo.
- `MantImpMarca` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:544`; condiciones en catálogo.
- `MantImpModelo` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:546`; condiciones en catálogo.
- `MantImpresora` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:548`; condiciones en catálogo.
- `MantProvSuc` (intent_candidate) — `app/src/main/java/com/dtsgt/mant/Lista.java:550`; condiciones en catálogo.

## Estado global escrito

`banco`, `disc`, `gcods`, `listaedit`, `mantid`, `pickcode`, `pickname`, `savemantid`

## Tablas mencionadas estáticamente

`FPRINT`, `P_ARCHIVOCONF`, `P_BANCO`, `P_CLIENTE`, `P_CONCEPTOPAGO`, `P_CORREL_OTROS`, `P_DESCUENTO`, `P_EMPRESA`, `P_ESTACION`, `P_IMPRESORA`, `P_IMPRESORA_MARCA`, `P_IMPRESORA_MODELO`, `P_IMPUESTO`, `P_LINEA`, `P_MEDIAPAGO`, `P_MONEDA`, `P_MOTIVO_AJUSTE`, `P_NIVELPRECIO`, `P_PRODOPC`, `P_PRODUCTO`, `P_PROVEEDOR`, `P_PROVEEDOR_SUCURSAL`, `P_RES_GRUPO`, `P_RES_MESA`, `P_RES_SALA`, `P_RUTA`, `P_SUCURSAL`, `VENDEDORES`

## Métodos

- `onCreate` — línea 42.
- `doAdd` — línea 82.
- `doClear` — línea 87.
- `doExit` — línea 91.
- `setHandlers` — línea 95.
- `onItemClick` — línea 98.
- `afterTextChanged` — línea 138.
- `beforeTextChanged` — línea 140.
- `onTextChanged` — línea 142.
- `listItems` — línea 153.
- `setTableSQL` — línea 204.
- `setMantID` — línea 421.
- `abrirMant` — línea 491.
- `listFPrints` — línea 557.
- `onResume` — línea 594.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

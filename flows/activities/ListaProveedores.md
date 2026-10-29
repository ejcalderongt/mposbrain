# ListaProveedores

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/ListaProveedores.java:24`; hereda `PBase`.

## Layouts candidatos

- `activity_lista_proveedores` — `app/src/main/java/com/dtsgt/mpos/ListaProveedores.java:43`.

## Navegación candidata

- `MantProveedor` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaProveedores.java:87`; condiciones en catálogo.
- `Producto` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaProveedores.java:118`; condiciones en catálogo.

## Estado global escrito

`cod_prov_recarga`, `gcods`, `listaedit`, `mantid`, `pickcode`, `pickname`, `savemantid`

## Tablas mencionadas estáticamente

`P_PROVEEDOR`

## Métodos

- `onCreate` — línea 40.
- `doAdd` — línea 77.
- `abrirMant` — línea 82.
- `doClear` — línea 91.
- `doExit` — línea 95.
- `setHandlers` — línea 99.
- `onItemClick` — línea 102.
- `afterTextChanged` — línea 130.
- `beforeTextChanged` — línea 132.
- `onTextChanged` — línea 134.
- `listItems` — línea 145.
- `setTableSQL` — línea 187.
- `onResume` — línea 203.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

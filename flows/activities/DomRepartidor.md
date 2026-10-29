# DomRepartidor

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/DomRepartidor.java:22`; hereda `PBase`.

## Layouts candidatos

- `activity_dom_repartidor` — `app/src/main/java/com/dtsgt/mpos/DomRepartidor.java:41`.

## Navegación candidata

- `DomRepartDet` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DomRepartidor.java:74`; condiciones en catálogo.
- `DomRepartDet` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DomRepartidor.java:104`; condiciones en catálogo.

## Estado global escrito

`dialogr`, `gint`, `gstr`, `gstr2`, `ped_dom_empresa`, `repartidor_codigo`

## Tablas mencionadas estáticamente

No detectadas.

## Métodos

- `onCreate` — línea 36.
- `doAdd` — línea 72.
- `doClear` — línea 77.
- `doExit` — línea 81.
- `setHandlers` — línea 85.
- `onItemClick` — línea 88.
- `onCheckedChanged` — línea 110.
- `afterTextChanged` — línea 119.
- `beforeTextChanged` — línea 121.
- `onTextChanged` — línea 123.
- `listItems` — línea 134.
- `dialogswitch` — línea 173.
- `cargaEmpresas` — línea 189.
- `nombreEmpresa` — línea 208.
- `onResume` — línea 219.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

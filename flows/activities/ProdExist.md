# ProdExist

Dominio: `inventory`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/ProdExist.java:20`; hereda `PBase`.

## Layouts candidatos

- `activity_prod_exist` — `app/src/main/java/com/dtsgt/mpos/ProdExist.java:36`.

## Navegación candidata

- `ProdExistList` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ProdExist.java:185`; condiciones en catálogo.

## Estado global escrito

`pprodname`, `prodcod`

## Tablas mencionadas estáticamente

`P_PRODUCTO`

## Métodos

- `onCreate` — línea 31.
- `porCodigo` — línea 58.
- `porNombre` — línea 68.
- `setHandlers` — línea 78.
- `afterTextChanged` — línea 99.
- `beforeTextChanged` — línea 101.
- `onTextChanged` — línea 103.
- `listItems` — línea 123.
- `msgAskExist` — línea 176.
- `onClick` — línea 184.
- `onClick` — línea 190.
- `ltrim` — línea 203.
- `limpiaFiltro` — línea 222.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

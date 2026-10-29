# ListaBarril

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/ListaBarril.java:21`; hereda `PBase`.

## Layouts candidatos

- `activity_lista_barril` — `app/src/main/java/com/dtsgt/mpos/ListaBarril.java:37`.

## Navegación candidata

- `MantBarril` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaBarril.java:77`; condiciones en catálogo.
- `MantBarril` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ListaBarril.java:101`; condiciones en catálogo.

## Estado global escrito

`gcods`

## Tablas mencionadas estáticamente

`D_BARRIL`

## Métodos

- `onCreate` — línea 34.
- `doAdd` — línea 74.
- `doProd` — línea 83.
- `doEst` — línea 87.
- `setHandlers` — línea 91.
- `onItemClick` — línea 94.
- `listItems` — línea 110.
- `listProd` — línea 155.
- `onItemClick` — línea 168.
- `onClick` — línea 179.
- `listEstado` — línea 191.
- `onItemClick` — línea 203.
- `onClick` — línea 214.
- `nombreProd` — línea 226.
- `nombreTipo` — línea 239.
- `nombreEst` — línea 252.
- `onResume` — línea 284.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

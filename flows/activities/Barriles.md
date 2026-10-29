# Barriles

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/Barriles.java:26`; hereda `PBase`.

## Layouts candidatos

- `activity_barriles` — `app/src/main/java/com/dtsgt/mpos/Barriles.java:49`.

## Navegación candidata

- `BarrilesDisponibles` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Barriles.java:187`; condiciones en catálogo.

## Estado global escrito

`gcods`, `modo_apertura`

## Tablas mencionadas estáticamente

`D_BARRIL`

## Métodos

- `onCreate` — línea 46.
- `run` — línea 67.
- `doOpen` — línea 81.
- `doReopen` — línea 87.
- `doDel` — línea 93.
- `setHandlers` — línea 102.
- `onItemClick` — línea 105.
- `listItems` — línea 121.
- `listaDisponibles` — línea 151.
- `onItemClick` — línea 183.
- `onClick` — línea 194.
- `abreBarril` — línea 206.
- `reabreBarril` — línea 229.
- `cierraBarril` — línea 251.
- `sendBarrilItem` — línea 275.
- `confirmCallback` — línea 289.
- `addItemSqlAndroid` — línea 303.
- `nombreProd` — línea 332.
- `nombreTipo` — línea 345.
- `nombreEst` — línea 358.
- `cierreDlg` — línea 385.
- `onItemClick` — línea 395.
- `onClick` — línea 406.
- `msgAskCierre` — línea 419.
- `onClick` — línea 426.
- `onClick` — línea 432.
- `onResume` — línea 443.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

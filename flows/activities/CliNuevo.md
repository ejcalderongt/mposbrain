# CliNuevo

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CliNuevo.java:29`; hereda `PBase`.

## Layouts candidatos

- `activity_cli_nuevo` — `app/src/main/java/com/dtsgt/mpos/CliNuevo.java:58`.

## Navegación candidata

- `CliDet` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliNuevo.java:276`; condiciones en catálogo.

## Estado global escrito

`cliente`, `credito`

## Tablas mencionadas estáticamente

`P_NIVELPRECIO`

## Métodos

- `onCreate` — línea 54.
- `onLocationChanged` — línea 82.
- `onProviderDisabled` — línea 86.
- `onProviderEnabled` — línea 90.
- `onStatusChanged` — línea 94.
- `run` — línea 102.
- `doSave` — línea 112.
- `setHandlers` — línea 133.
- `onItemSelected` — línea 138.
- `onNothingSelected` — línea 162.
- `saveData` — línea 171.
- `lastKnowPos` — línea 293.
- `getLocation` — línea 311.
- `fillSpinner` — línea 376.
- `checkValues` — línea 412.
- `valToStr` — línea 469.
- `msgAskSave` — línea 473.
- `onClick` — línea 481.
- `onClick` — línea 487.
- `onClick` — línea 493.
- `msgAskExit` — línea 506.
- `onClick` — línea 514.
- `onClick` — línea 520.
- `doExit` — línea 533.
- `onBackPressed` — línea 545.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

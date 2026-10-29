# Deposito

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/Deposito.java:38`; hereda `PBase`.

## Layouts candidatos

- `activity_deposito` — `app/src/main/java/com/dtsgt/mpos/Deposito.java:70`.

## Navegación candidata

- `DesgloseMon` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Deposito.java:113`; condiciones en catálogo.

## Estado global escrito

`gint`, `totDep`, `validimp`

## Tablas mencionadas estáticamente

`D_FACTURA`, `D_FACTURAP`, `P_BANCO`, `P_DEPOSITO`, `T_DEPOSB`

## Métodos

- `onCreate` — línea 65.
- `doSave` — línea 103.
- `doDesglose` — línea 111.
- `doExit` — línea 119.
- `setHandlers` — línea 127.
- `onItemSelected` — línea 130.
- `onNothingSelected` — línea 150.
- `guardaDeposito` — línea 163.
- `finishDoc` — línea 209.
- `msgAskSave` — línea 226.
- `onClick` — línea 234.
- `onClick` — línea 240.
- `msgAskExit` — línea 253.
- `onClick` — línea 263.
- `onClick` — línea 269.
- `desglose` — línea 286.
- `fillDocList` — línea 373.
- `fillSpinner` — línea 414.
- `checkValues` — línea 444.
- `onResume` — línea 473.
- `onBackPressed` — línea 483.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

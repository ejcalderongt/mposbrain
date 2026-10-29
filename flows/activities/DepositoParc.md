# DepositoParc

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/DepositoParc.java:30`; hereda `PBase`.

## Layouts candidatos

- `activity_deposito_parc` — `app/src/main/java/com/dtsgt/mpos/DepositoParc.java:53`.
- `activity_depos_doc` — `app/src/main/java/com/dtsgt/mpos/DepositoParc.java:187`.

## Navegación candidata

- `Desglose` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DepositoParc.java:107`; condiciones en catálogo.

## Estado global escrito

`totDep`

## Tablas mencionadas estáticamente

`D_COBRO`, `D_COBROP`, `D_DEPOS`, `D_FACTURA`, `D_FACTURAP`, `P_BANCO`, `T_DEPOSB`

## Métodos

- `onCreate` — línea 50.
- `listaDoc` — línea 86.
- `saveDepos` — línea 95.
- `OpenDesglose` — línea 104.
- `setHandlers` — línea 116.
- `onItemSelected` — línea 119.
- `onNothingSelected` — línea 138.
- `scanValues` — línea 147.
- `showDocDialog` — línea 182.
- `onItemClick` — línea 199.
- `onClick` — línea 219.
- `onClick` — línea 227.
- `fillDocList` — línea 240.
- `saveDoc` — línea 308.
- `fillSpinner` — línea 466.
- `setLimit` — línea 500.
- `checkValues` — línea 542.
- `msgAskSave` — línea 581.
- `onClick` — línea 591.
- `onClick` — línea 597.
- `msgAskExit` — línea 610.
- `onClick` — línea 620.
- `onClick` — línea 626.
- `doExit` — línea 639.
- `onBackPressed` — línea 651.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

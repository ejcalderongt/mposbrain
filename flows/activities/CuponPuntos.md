# CuponPuntos

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CuponPuntos.java:16`; hereda `PBase`.

## Layouts candidatos

- `activity_cupon_puntos` — `app/src/main/java/com/dtsgt/mpos/CuponPuntos.java:34`.

## Navegación candidata

- `CuponEnvios` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CuponPuntos.java:59`; condiciones en catálogo.

## Estado global escrito

`cliente_lealtad`

## Tablas mencionadas estáticamente

No detectadas.

## Métodos

- `onCreate` — línea 29.
- `doCupon` — línea 56.
- `doExit` — línea 66.
- `loadItem` — línea 74.
- `showItem` — línea 87.
- `setIdle` — línea 142.
- `onBackPressed` — línea 150.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

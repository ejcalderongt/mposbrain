# CuponEnvios

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CuponEnvios.java:32`; hereda `PBase`.

## Layouts candidatos

- `activity_cupon_envios` — `app/src/main/java/com/dtsgt/mpos/CuponEnvios.java:59`.

## Navegación candidata

- `CuponNuevo` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CuponEnvios.java:530`; condiciones en catálogo.

## Estado global escrito

`cliente_lealtad`, `codigo_cupon_correo`, `puntos_disponibles`

## Tablas mencionadas estáticamente

`D_LEAL_CAMBIO`, `D_LEAL_EMISION`

## Métodos

- `onCreate` — línea 55.
- `doExit` — línea 103.
- `listItems` — línea 111.
- `terminaRegistros` — línea 134.
- `procesaPuntos` — línea 158.
- `registraPunto` — línea 167.
- `cbRegistraPunto` — línea 189.
- `terminaPuntos` — línea 213.
- `procesaCupones` — línea 225.
- `registraCupon` — línea 238.
- `cbRegistraCupon` — línea 275.
- `terminaCupones` — línea 299.
- `consultaPuntos` — línea 311.
- `cbConsultaPuntos` — línea 327.
- `validaCriteria` — línea 360.
- `enviaCupon` — línea 391.
- `procesaEnviaCupon` — línea 414.
- `sendgmail` — línea 442.
- `splitInTwo` — línea 475.
- `confirmaEnvio` — línea 509.
- `msgAskEmitir` — línea 523.
- `msgAskSent` — línea 544.
- `setidle` — línea 562.
- `finishok` — línea 567.
- `finishError` — línea 576.
- `finishErrList` — línea 586.
- `addError` — línea 596.
- `onResume` — línea 604.
- `onBackPressed` — línea 627.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

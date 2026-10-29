# CuponFisicoEnvios

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CuponFisicoEnvios.java:24`; hereda `PBase`.

## Layouts candidatos

- `activity_cupon_fisico_envios` — `app/src/main/java/com/dtsgt/mpos/CuponFisicoEnvios.java:55`.

## Navegación candidata

- `CuponVirEnvio` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CuponFisicoEnvios.java:157`; condiciones en catálogo.

## Estado global escrito

`cupon_codigo`

## Tablas mencionadas estáticamente

`D_BILLETERA_PAGO`, `D_CUPON_ACTIV`, `D_LEAL_CAMBIO`, `D_LEAL_CUPON`

## Métodos

- `onCreate` — línea 50.
- `doExit` — línea 97.
- `listItems` — línea 105.
- `terminaEnvios` — línea 140.
- `tarjetaCorreo` — línea 154.
- `procesaTarjetaFisica` — línea 170.
- `registraTarjetaFisica` — línea 183.
- `cbRegistraTarjetasFisicas` — línea 221.
- `terminaTarjetasFisicas` — línea 245.
- `procesaTarjetaVirtual` — línea 263.
- `registraTarjetaVirtual` — línea 276.
- `cbRegistraTarjetaVirtual` — línea 314.
- `terminaTarjetasVirtuales` — línea 338.
- `procesaPuntos` — línea 354.
- `registraPuntos` — línea 367.
- `cbRegistraPuntos` — línea 389.
- `terminaPuntos` — línea 413.
- `procesaBilletera` — línea 425.
- `registraBilletera` — línea 438.
- `cbRegistraBilletera` — línea 461.
- `terminaBilletera` — línea 486.
- `setidle` — línea 503.
- `finishok` — línea 508.
- `finishError` — línea 517.
- `finishErrList` — línea 527.
- `addError` — línea 537.
- `validaEnvioTarjetas` — línea 541.
- `onResume` — línea 556.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

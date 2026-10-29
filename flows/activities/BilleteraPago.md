# BilleteraPago

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/BilleteraPago.java:21`; hereda `PBase`.

## Layouts candidatos

- `activity_billetera_pago` — `app/src/main/java/com/dtsgt/mpos/BilleteraPago.java:39`.

## Navegación candidata


## Estado global escrito

No detectado.

## Tablas mencionadas estáticamente

`D_BILLETERA_PAGO`, `T_PAGO`

## Métodos

- `onCreate` — línea 34.
- `doSave` — línea 68.
- `doExit` — línea 83.
- `loadItem` — línea 91.
- `showItem` — línea 153.
- `aplicaPago` — línea 198.
- `msgAskAplicar` — línea 231.
- `onClick` — línea 238.
- `onClick` — línea 244.
- `setIdle` — línea 255.
- `setBusy` — línea 259.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

# DomPago

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/DomPago.java:18`; hereda `PBase`.

## Layouts candidatos

- `activity_dom_pago` — `app/src/main/java/com/dtsgt/mpos/DomPago.java:36`.

## Navegación candidata

- `srvCommit` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DomPago.java:248`; condiciones en catálogo.

## Estado global escrito

`dialogr`

## Tablas mencionadas estáticamente

`D_DOMICILIO_ENC`, `D_DOMICILIO_ENTREGA`, `D_FACTURAP`, `P_MEDIAPAGO`

## Métodos

- `onCreate` — línea 32.
- `doApply` — línea 64.
- `doExit` — línea 76.
- `setHandlers` — línea 80.
- `afterTextChanged` — línea 84.
- `beforeTextChanged` — línea 86.
- `onTextChanged` — línea 88.
- `afterTextChanged` — línea 95.
- `beforeTextChanged` — línea 97.
- `onTextChanged` — línea 99.
- `loadItem` — línea 110.
- `saveItem` — línea 130.
- `enviaEstadoCompleto` — línea 227.
- `dialogswitch` — línea 263.
- `calculaPago` — línea 279.
- `onResume` — línea 317.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

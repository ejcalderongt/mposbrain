# PedidoCli

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/PedidoCli.java:17`; hereda `PBase`.

## Layouts candidatos

- `activity_pedido_cli` — `app/src/main/java/com/dtsgt/mpos/PedidoCli.java:34`.
- `activity_pedido_cli_ver` — `app/src/main/java/com/dtsgt/mpos/PedidoCli.java:36`.

## Navegación candidata

- `srvPedidoDir` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/PedidoCli.java:166`; condiciones en catálogo.

## Estado global escrito

No detectado.

## Tablas mencionadas estáticamente

`D_PEDIDO`

## Métodos

- `onCreate` — línea 29.
- `doSave` — línea 58.
- `setHandlers` — línea 66.
- `beforeTextChanged` — línea 69.
- `onTextChanged` — línea 71.
- `afterTextChanged` — línea 73.
- `beforeTextChanged` — línea 80.
- `onTextChanged` — línea 82.
- `afterTextChanged` — línea 84.
- `beforeTextChanged` — línea 91.
- `onTextChanged` — línea 93.
- `afterTextChanged` — línea 95.
- `beforeTextChanged` — línea 102.
- `onTextChanged` — línea 104.
- `afterTextChanged` — línea 106.
- `beforeTextChanged` — línea 113.
- `onTextChanged` — línea 115.
- `afterTextChanged` — línea 117.
- `doExit` — línea 125.
- `loadItem` — línea 133.
- `saveItem` — línea 151.
- `checkItem` — línea 186.
- `isEmpty` — línea 217.
- `aplicaCF` — línea 233.
- `pantallaHorizontal` — línea 254.
- `msgAskExit` — línea 268.
- `onClick` — línea 275.
- `onClick` — línea 281.
- `msgAskCF` — línea 288.
- `onClick` — línea 295.
- `onClick` — línea 301.
- `msgAskSave` — línea 308.
- `onClick` — línea 315.
- `onClick` — línea 321.
- `onResume` — línea 332.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

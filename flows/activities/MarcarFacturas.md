# MarcarFacturas

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/MarcarFacturas.java:28`; hereda `PBase`.

## Layouts candidatos

- `activity_marcar_facturas` — `app/src/main/java/com/dtsgt/mpos/MarcarFacturas.java:64`.

## Navegación candidata


## Estado global escrito

No detectado.

## Tablas mencionadas estáticamente

`D_FACTURA`, `P_CLIENTE`

## Métodos

- `onCreate` — línea 61.
- `anulDoc` — línea 89.
- `setHandlers` — línea 100.
- `onSwipeRight` — línea 104.
- `onSwipeLeft` — línea 107.
- `onItemClick` — línea 111.
- `onItemLongClick` — línea 130.
- `listItems` — línea 159.
- `aplicaBandera` — línea 237.
- `showDateDialog1` — línea 262.
- `showDateDialog2` — línea 272.
- `obtenerFecha` — línea 282.
- `onDateSet` — línea 285.
- `setFechaAct` — línea 339.
- `msgAsk1` — línea 359.
- `onClick` — línea 366.
- `onClick` — línea 372.
- `msgAsk2` — línea 379.
- `msgExit` — línea 390.
- `strfechasinhora` — línea 402.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

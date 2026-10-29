# CajaPagosPend

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CajaPagosPend.java:19`; hereda `PBase`.

## Layouts candidatos

- `activity_caja_pagos_pend` — `app/src/main/java/com/dtsgt/mpos/CajaPagosPend.java:36`.

## Navegación candidata

- `ValidaSuper` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaPagosPend.java:70`; condiciones en catálogo.

## Estado global escrito

`tipo`

## Tablas mencionadas estáticamente

`D_FACTURA`, `D_FACTURAP`, `P_CLIENTE`

## Métodos

- `onCreate` — línea 33.
- `anulDoc` — línea 58.
- `setHandlers` — línea 80.
- `onSwipeRight` — línea 84.
- `onSwipeLeft` — línea 87.
- `onItemClick` — línea 91.
- `onItemLongClick` — línea 110.
- `listItems` — línea 138.
- `pagarDocumento` — línea 240.
- `aplicarPago` — línea 253.
- `msgAsk` — línea 269.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

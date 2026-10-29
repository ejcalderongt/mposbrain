# DepositoLista

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/DepositoLista.java:20`; hereda `PBase`.

## Layouts candidatos

- `activity_deposito_lista` — `app/src/main/java/com/dtsgt/mpos/DepositoLista.java:47`.

## Navegación candidata

- `Deposito` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DepositoLista.java:76`; condiciones en catálogo.
- `PrintView` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DepositoLista.java:137`; condiciones en catálogo.

## Estado global escrito

No detectado.

## Tablas mencionadas estáticamente

No detectadas.

## Métodos

- `onCreate` — línea 43.
- `doAdd` — línea 74.
- `doExit` — línea 79.
- `setHandlers` — línea 83.
- `onItemClick` — línea 87.
- `listItems` — línea 113.
- `printDocument` — línea 132.
- `showDateDialog1` — línea 152.
- `showDateDialog2` — línea 163.
- `obtenerFecha` — línea 173.
- `onDateSet` — línea 181.
- `setFechaAct` — línea 213.
- `nombreBanco` — línea 235.
- `onResume` — línea 254.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

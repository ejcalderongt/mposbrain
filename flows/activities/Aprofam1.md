# Aprofam1

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/Aprofam1.java:15`; hereda `PBase`.

## Layouts candidatos

- `activity_aprofam1` — `app/src/main/java/com/dtsgt/mpos/Aprofam1.java:31`.

## Navegación candidata

- `Venta` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/Aprofam1.java:76`; condiciones en catálogo.

## Estado global escrito

`gDirCliente`, `gNITCliente`, `gNombreCliente`, `ref1`, `ref2`, `ref3`

## Tablas mencionadas estáticamente

No detectadas.

## Métodos

- `onCreate` — línea 28.
- `doVenta` — línea 52.
- `doExit` — línea 84.
- `setHandlers` — línea 93.
- `onItemSelected` — línea 96.
- `onNothingSelected` — línea 121.
- `onItemSelected` — línea 129.
- `onNothingSelected` — línea 154.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

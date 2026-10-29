# CliPosGTSel

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CliPosGTSel.java:8`; hereda `PBase`.

## Layouts candidatos

- `activity_cli_pos_gtsel` — `app/src/main/java/com/dtsgt/mpos/CliPosGTSel.java:14`.

## Navegación candidata

- `CliPos` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliPosGTSel.java:24`; condiciones en catálogo.
- `CliPos` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliPosGTSel.java:34`; condiciones en catálogo.

## Estado global escrito

`clipos_cf`

## Tablas mencionadas estáticamente

No detectadas.

## Métodos

- `onCreate` — línea 10.
- `doCF` — línea 21.
- `doFactura` — línea 31.
- `doExit` — línea 41.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

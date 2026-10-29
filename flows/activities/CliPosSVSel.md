# CliPosSVSel

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CliPosSVSel.java:13`; hereda `PBase`.

## Layouts candidatos

- `activity_cli_pos_svsel` — `app/src/main/java/com/dtsgt/mpos/CliPosSVSel.java:27`.

## Navegación candidata

- `CliPosSVCons` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliPosSVSel.java:66`; condiciones en catálogo.
- `CliPosSVCred` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliPosSVSel.java:92`; condiciones en catálogo.

## Estado global escrito

`domicilio`, `gNITCliente`, `parallevar`, `sv_cli_nue`, `sv_flag_ncr`, `sv_flag_nit`

## Tablas mencionadas estáticamente

No detectadas.

## Métodos

- `onCreate` — línea 23.
- `doNIT` — línea 49.
- `doNRC` — línea 76.
- `doExit` — línea 102.
- `setHandlers` — línea 106.
- `onCheckedChanged` — línea 109.
- `onCheckedChanged` — línea 117.
- `buscaNIT` — línea 131.
- `buscaNRC` — línea 143.
- `nitnumsv` — línea 157.
- `testNIT` — línea 175.
- `testDUI` — línea 186.
- `validaDUI` — línea 201.
- `testNRC` — línea 232.
- `onResume` — línea 253.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

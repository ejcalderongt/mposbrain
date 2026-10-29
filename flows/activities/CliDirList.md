# CliDirList

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CliDirList.java:21`; hereda `PBase`.

## Layouts candidatos

- `activity_cli_dir_list` — `app/src/main/java/com/dtsgt/mpos/CliDirList.java:39`.

## Navegación candidata

- `CliDirDom` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliDirList.java:73`; condiciones en catálogo.
- `CliDirDom` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliDirList.java:103`; condiciones en catálogo.

## Estado global escrito

`dom_ddir`, `idclidir`

## Tablas mencionadas estáticamente

`P_CLIENTE_DIR`

## Métodos

- `onCreate` — línea 36.
- `run` — línea 52.
- `doAdd` — línea 70.
- `setHandlers` — línea 76.
- `onItemClick` — línea 79.
- `onItemLongClick` — línea 92.
- `listItems` — línea 117.
- `loadDirs` — línea 130.
- `procesaDirecciones` — línea 140.
- `onResume` — línea 207.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

# SoporteEquNuevo

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/SoporteEquNuevo.java:32`; hereda `PBase`.

## Layouts candidatos

- `activity_soporte_equ_nuevo` — `app/src/main/java/com/dtsgt/mpos/SoporteEquNuevo.java:46`.

## Navegación candidata

- `WSRec` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/SoporteEquNuevo.java:163`; condiciones en catálogo.
- `SoporteCorel` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/SoporteEquNuevo.java:184`; condiciones en catálogo.

## Estado global escrito

`auto_run_venta`, `dialogr`, `estado_correl`, `estado_recep`, `recibir_automatico`

## Tablas mencionadas estáticamente

No detectadas.

## Métodos

- `onCreate` — línea 40.
- `doPaso1` — línea 74.
- `doPaso2` — línea 83.
- `doPaso3` — línea 95.
- `doPaso4` — línea 107.
- `doExit` — línea 119.
- `initSession` — línea 127.
- `paso1` — línea 140.
- `recepcionBaseDatos` — línea 148.
- `paso2` — línea 156.
- `validaPaso2` — línea 169.
- `paso3` — línea 178.
- `validaPaso3` — línea 190.
- `paso4` — línea 199.
- `dialogswitch` — línea 213.
- `msgAsk1` — línea 228.
- `msgAsk2` — línea 241.
- `msgAsk3` — línea 255.
- `msgAsk4` — línea 269.
- `msgExit` — línea 282.
- `run` — línea 285.
- `onClick` — línea 294.
- `showflags` — línea 310.
- `descargarDB` — línea 342.
- `descMsgEstado` — línea 376.
- `run` — línea 378.
- `unzip` — línea 386.
- `onResume` — línea 415.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

# RepesajeLista

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/RepesajeLista.java:17`; hereda `PBase`.

## Layouts candidatos

- `activity_repesaje_lista` — `app/src/main/java/com/dtsgt/mpos/RepesajeLista.java:33`.

## Navegación candidata

- `Repesaje` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/RepesajeLista.java:70`; condiciones en catálogo.

## Estado global escrito

No detectado.

## Tablas mencionadas estáticamente

`T_BARRA`, `T_VENTA`

## Métodos

- `onCreate` — línea 30.
- `repesaje` — línea 62.
- `exit` — línea 77.
- `setHandlers` — línea 81.
- `onItemClick` — línea 85.
- `listItems` — línea 111.
- `listItemsSingle` — línea 119.
- `listItemsBarra` — línea 152.
- `onResume` — línea 203.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

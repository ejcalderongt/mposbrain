# ValidaClave

Dominio: `sync-configuration`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/ValidaClave.java:20`; hereda `PBase`.

## Layouts candidatos

- `activity_valida_clave` — `app/src/main/java/com/dtsgt/mpos/ValidaClave.java:40`.
- `activity_valida_clave_ver` — `app/src/main/java/com/dtsgt/mpos/ValidaClave.java:42`.

## Navegación candidata

- `CuentasAbiertas` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ValidaClave.java:104`; condiciones en catálogo.
- `ResMesero` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ValidaClave.java:136`; condiciones en catálogo.
- `ResCaja` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ValidaClave.java:141`; condiciones en catálogo.
- `ResMesero` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ValidaClave.java:238`; condiciones en catálogo.
- `ResCaja` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ValidaClave.java:240`; condiciones en catálogo.
- `ResCaja` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ValidaClave.java:265`; condiciones en catálogo.

## Estado global escrito

`cierra_clave`, `idmesero`, `meserodir`, `nombre_mesero_sel`

## Tablas mencionadas estáticamente

`P_RUTA`, `P_VENDEDOR_ROL`, `T_ORDEN`, `T_ORDENCOMBO`, `T_ORDENCOMBOAD`, `T_ORDENCOMBODET`, `T_ORDENCOMBOPRECIO`, `T_ORDENCUENTA`, `T_ORDEN_ING`, `VENDEDORES`

## Métodos

- `onCreate` — línea 32.
- `doKey` — línea 86.
- `doCuentas` — línea 102.
- `doExit` — línea 110.
- `setHandlers` — línea 115.
- `onItemClick` — línea 120.
- `listItems` — línea 162.
- `validaClave` — línea 217.
- `pantallaHorizontal` — línea 252.
- `autoStartCajero` — línea 262.
- `botonCuentas` — línea 273.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

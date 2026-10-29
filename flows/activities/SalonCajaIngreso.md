# SalonCajaIngreso

Dominio: `restaurant`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/SalonCajaIngreso.java:24`; hereda `PBase`.

## Layouts candidatos

- `activity_salon_caja_ingreso` — `app/src/main/java/com/dtsgt/mpos/SalonCajaIngreso.java:43`.

## Navegación candidata

- `SalonRecepcion` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/SalonCajaIngreso.java:108`; condiciones en catálogo.
- `ResMesero` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/SalonCajaIngreso.java:140`; condiciones en catálogo.
- `ResCaja` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/SalonCajaIngreso.java:145`; condiciones en catálogo.
- `ResMesero` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/SalonCajaIngreso.java:242`; condiciones en catálogo.
- `ResCaja` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/SalonCajaIngreso.java:244`; condiciones en catálogo.
- `ResCaja` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/SalonCajaIngreso.java:269`; condiciones en catálogo.

## Estado global escrito

`cierra_clave`, `idmesero`, `meserodir`, `nombre_mesero_sel`

## Tablas mencionadas estáticamente

`P_RUTA`, `P_VENDEDOR_ROL`, `T_ORDEN`, `T_ORDENCOMBO`, `T_ORDENCOMBOAD`, `T_ORDENCOMBODET`, `T_ORDENCOMBOPRECIO`, `T_ORDENCUENTA`, `T_ORDEN_ING`, `VENDEDORES`

## Métodos

- `onCreate` — línea 36.
- `doKey` — línea 90.
- `doCuentas` — línea 106.
- `doExit` — línea 114.
- `setHandlers` — línea 119.
- `onItemClick` — línea 124.
- `listItems` — línea 166.
- `validaClave` — línea 221.
- `pantallaHorizontal` — línea 256.
- `autoStartCajero` — línea 266.
- `botonCuentas` — línea 277.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

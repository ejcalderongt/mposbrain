# SalonRecepcion

Dominio: `restaurant`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/SalonRecepcion.java:43`; hereda `PBase`.

## Layouts candidatos

- `activity_salon_recepcion` — `app/src/main/java/com/dtsgt/mpos/SalonRecepcion.java:80`.

## Navegación candidata


## Estado global escrito

`cierra_clave`, `idmesero`, `idorden`, `timeout`, `wsurl`

## Tablas mencionadas estáticamente

`D_ORDEN_COREL`, `P_RES_SESION_ID_COR`, `P_RUTA`, `P_VENDEDOR_ROL`, `VENDEDORES`

## Métodos

- `onCreate` — línea 74.
- `doSave` — línea 132.
- `doExit` — línea 158.
- `setHandlers` — línea 163.
- `onItemClick` — línea 168.
- `onItemClick` — línea 185.
- `listItems` — línea 212.
- `run` — línea 269.
- `creaSession` — línea 300.
- `cbResSesionList` — línea 309.
- `registraCita` — línea 340.
- `addOrden` — línea 350.
- `agregaOrden` — línea 446.
- `PutCorelCallback` — línea 461.
- `GetCorelCallback` — línea 475.
- `getURL` — línea 512.
- `pantallaHorizontal` — línea 538.
- `msgAskApply` — línea 552.
- `onClick` — línea 560.
- `onClick` — línea 566.
- `onResume` — línea 579.
- `onBackPressed` — línea 599.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

# Pago

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/Pago.java:28`; hereda `PBase`.

## Layouts candidatos

- `activity_pago` — `app/src/main/java/com/dtsgt/mpos/Pago.java:58`.

## Navegación candidata


## Estado global escrito

`brw`, `pagado`

## Tablas mencionadas estáticamente

`P_BANCO`, `P_CLIENTE`, `P_MEDIAPAGO`, `T_PAGO`, `T_PAGOD`

## Métodos

- `onCreate` — línea 55.
- `addPayment` — línea 96.
- `deletePayment` — línea 131.
- `savePago` — línea 145.
- `setHandlers` — línea 162.
- `onItemClick` — línea 166.
- `listItems` — línea 193.
- `addPago` — línea 230.
- `delPago` — línea 275.
- `initSession` — línea 289.
- `finalCheck` — línea 307.
- `selPago` — línea 334.
- `listPagos` — línea 367.
- `showPagoDialog` — línea 425.
- `listBancos` — línea 474.
- `showBancoDialog` — línea 511.
- `inputNumero` — línea 558.
- `onClick` — línea 578.
- `onClick` — línea 589.
- `checkNum` — línea 601.
- `aplicarFecha` — línea 626.
- `obtenerFecha` — línea 639.
- `onDateSet` — línea 642.
- `setActDate` — línea 659.
- `setNivel` — línea 675.
- `totalPago` — línea 695.
- `actMonto` — línea 709.
- `doExit` — línea 728.
- `msgAskOverPayd` — línea 740.
- `onClick` — línea 751.
- `onClick` — línea 757.
- `msgAskExit` — línea 770.
- `onClick` — línea 780.
- `onClick` — línea 786.
- `msgAskExit2` — línea 799.
- `onClick` — línea 809.
- `onClick` — línea 817.
- `msgAskSave` — línea 830.
- `onClick` — línea 841.
- `onClick` — línea 853.
- `msgAskSaveEmpty` — línea 865.
- `onClick` — línea 876.
- `onClick` — línea 883.
- `msgAskDel` — línea 895.
- `onClick` — línea 906.
- `onClick` — línea 912.
- `onBackPressed` — línea 928.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

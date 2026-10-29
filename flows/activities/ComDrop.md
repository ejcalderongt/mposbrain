# ComDrop

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/ComDrop.java:29`; hereda `Activity`.

## Layouts candidatos

- `activity_com_drop` — `app/src/main/java/com/dtsgt/mpos/ComDrop.java:54`.

## Navegación candidata

- `com.ttxapps.dropsync` (external_app_candidate) — `app/src/main/java/com/dtsgt/mpos/ComDrop.java:82`; condiciones en catálogo.
- `MessageBox` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ComDrop.java:482`; condiciones en catálogo.

## Estado global escrito

No detectado.

## Tablas mencionadas estáticamente

`D_ATENCION`, `D_COBRO`, `D_DEPOS`, `D_FACTURA`, `D_MOV`, `D_PEDIDO`, `P_COREL`

## Métodos

- `onCreate` — línea 51.
- `syncDropBox` — línea 80.
- `sendSMS` — línea 93.
- `callPhone` — línea 103.
- `runRecep` — línea 116.
- `runSend` — línea 140.
- `genData` — línea 151.
- `setFlags` — línea 321.
- `readDataHeader` — línea 449.
- `showmsg` — línea 479.
- `askRec` — línea 486.
- `onClick` — línea 492.
- `askSend` — línea 503.
- `onClick` — línea 509.
- `askSendOK` — línea 520.
- `onClick` — línea 526.
- `askSendOK2` — línea 537.
- `onClick` — línea 543.
- `onResume` — línea 557.
- `onPause` — línea 562.
- `onBackPressed` — línea 571.
- `opendb` — línea 578.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

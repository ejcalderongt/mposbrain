# comWSLic

Dominio: `sync-configuration`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/comWSLic.java:42`; hereda `PBase`.

## Layouts candidatos

- `activity_com_wslic` — `app/src/main/java/com/dtsgt/mpos/comWSLic.java:88`.

## Navegación candidata

- `ComDrop` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/comWSLic.java:758`; condiciones en catálogo.
- `this.getPackageName` (external_app_candidate) — `app/src/main/java/com/dtsgt/mpos/comWSLic.java:899`; condiciones en catálogo.

## Estado global escrito

`isOnWifi`

## Tablas mencionadas estáticamente

`PARAMS`, `P_RUTA`, `P_STOCK`

## Métodos

- `onCreate` — línea 85.
- `askSend` — línea 136.
- `onClick` — línea 150.
- `validaLicencia` — línea 165.
- `setHandlers` — línea 200.
- `onSwipeRight` — línea 202.
- `onSwipeLeft` — línea 206.
- `runSend` — línea 215.
- `fillTable` — línea 243.
- `commitSQL` — línea 332.
- `requestLicence` — línea 386.
- `requestLicenceRuta` — línea 432.
- `OpenDTt` — línea 472.
- `getTest` — línea 526.
- `sendData` — línea 564.
- `envioLic` — línea 583.
- `addItem` — línea 618.
- `wsSendExecute` — línea 639.
- `wsSendFinished` — línea 666.
- `comManual` — línea 756.
- `getWSURL` — línea 766.
- `setComParams` — línea 808.
- `getDocCount` — línea 837.
- `paramsExtra` — línea 867.
- `writeErrLog` — línea 877.
- `restarApp` — línea 896.
- `msgResultEnvio` — línea 911.
- `onClick` — línea 920.
- `msgAskExit` — línea 934.
- `onClick` — línea 943.
- `msgAskExitComplete` — línea 961.
- `onClick` — línea 970.
- `onClick` — línea 976.
- `onBackPressed` — línea 995.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

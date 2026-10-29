# DevolCli

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/DevolCli.java:26`; hereda `PBase`.

## Layouts candidatos

- `activity_devol_cli` — `app/src/main/java/com/dtsgt/mpos/DevolCli.java:50`.

## Navegación candidata

- `Producto` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DevolCli.java:114`; condiciones en catálogo.
- `DevCliCant` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DevolCli.java:222`; condiciones en catálogo.
- `DevCliCant` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DevolCli.java:253`; condiciones en catálogo.
- `CliDet` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/DevolCli.java:501`; condiciones en catálogo.

## Estado global escrito

`brw`, `devrazon`, `devtipo`, `dvactuald`, `dvactualnc`, `dvbrowse`, `dvcorreld`, `dvcorrelnc`, `dvdispventa`, `dvestado`, `dvfactor`, `dvlote`, `dvpeso`, `dvporpeso`, `dvprec`, `dvpreclista`, `dvtotal`, `dvumpeso`, `dvumstock`, `dvumventa`, `prod`, `tienelote`, `tiponcredito`

## Tablas mencionadas estáticamente

`D_NOTACRED`, `P_CORREL_OTROS`, `P_STOCK`, `T_CXCD`

## Métodos

- `onCreate` — línea 47.
- `run` — línea 76.
- `run` — línea 82.
- `run` — línea 89.
- `run` — línea 94.
- `showProd` — línea 109.
- `finishDevol` — línea 123.
- `setHandlers` — línea 139.
- `onItemClick` — línea 143.
- `onItemLongClick` — línea 159.
- `listItems` — línea 182.
- `processItem` — línea 199.
- `setCant` — línea 216.
- `updCant` — línea 230.
- `processCant` — línea 263.
- `addItem` — línea 282.
- `saveDevol` — línea 353.
- `createDoc` — línea 553.
- `delItem` — línea 582.
- `obtienecorrel` — línea 607.
- `clearData` — línea 641.
- `msgAskExit` — línea 650.
- `onClick` — línea 661.
- `onClick` — línea 668.
- `msgAskComplete` — línea 681.
- `onClick` — línea 691.
- `onClick` — línea 697.
- `msgAskDel` — línea 712.
- `onClick` — línea 721.
- `onClick` — línea 727.
- `askPrint` — línea 737.
- `onClick` — línea 745.
- `onClick` — línea 779.
- `hasProducts` — línea 793.
- `doExit` — línea 807.
- `limpiavariables_devol` — línea 822.
- `onResume` — línea 849.
- `onBackPressed` — línea 871.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

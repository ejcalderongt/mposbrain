# CliPosSVCred

Dominio: `sales-orders`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CliPosSVCred.java:22`; hereda `PBase`.

## Layouts candidatos

- `activity_cli_pos_svcred` — `app/src/main/java/com/dtsgt/mpos/CliPosSVCred.java:43`.

## Navegación candidata

- `CliPosSVGiro` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CliPosSVCred.java:97`; condiciones en catálogo.

## Estado global escrito

`cf_domicilio`, `cliente`, `cliente_credito`, `cliente_dom`, `codigo_cliente`, `contrib`, `dias_credito`, `dom_dir`, `dom_nit`, `dom_nom`, `dom_ref`, `dom_tel`, `gCorreoCliente`, `gDirCliente`, `gNITCliente`, `gNombreCliente`, `gTelCliente`, `limite_credito`, `media`, `mododocesa`, `nivel`, `percepcion`, `rutatipo`, `sal_NIT`, `sal_NRC`, `sal_PER`, `sal_dep`, `sal_iddep`, `sal_idmun`, `sal_idneg`, `sal_mun`, `sal_neg`, `scancliente`, `ventalock`

## Tablas mencionadas estáticamente

No detectadas.

## Métodos

- `onCreate` — línea 38.
- `doContinue` — línea 91.
- `doGiro` — línea 95.
- `doExit` — línea 100.
- `doDep` — línea 108.
- `doMuni` — línea 116.
- `guardaDatos` — línea 128.
- `cargaCliente` — línea 139.
- `listDepartamentos` — línea 158.
- `onItemClick` — línea 168.
- `onClick` — línea 181.
- `listMunicipios` — línea 193.
- `onItemClick` — línea 204.
- `onClick` — línea 216.
- `cargaDepartamentos` — línea 228.
- `cargaMunicipios` — línea 236.
- `agregaCliente` — línea 251.
- `procesaNIT` — línea 323.
- `cargaNRC` — línea 372.
- `guardaNRC` — línea 411.
- `cargaSeleccion` — línea 435.
- `guardaSeleccion` — línea 465.
- `validaDatos` — línea 495.
- `validaGiro` — línea 559.
- `asignaGiro` — línea 569.
- `nitnumsv` — línea 582.
- `testNIT` — línea 594.
- `onResume` — línea 644.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

# ResCliente

Dominio: `restaurant`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/ResCliente.java:30`; hereda `PBase`.

## Layouts candidatos

- `activity_res_cliente` — `app/src/main/java/com/dtsgt/mpos/ResCliente.java:61`.
- `activity_res_cliente_ver` — `app/src/main/java/com/dtsgt/mpos/ResCliente.java:63`.

## Navegación candidata

- `Clientes` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/ResCliente.java:179`; condiciones en catálogo.

## Estado global escrito

`cliente`, `codigo_cliente`, `contrib`, `dom_dir`, `dom_nit`, `dom_nom`, `dom_ref`, `dom_tel`, `gCorreoCliente`, `gDirCliente`, `gNITCliente`, `gNITcf`, `gNombreCliente`, `gTelCliente`, `media`, `nit_tipo`, `nivel`, `pedcorel`, `percepcion`, `rutatipo`, `sal_NIT`, `sal_NRC`, `sal_PER`, `scancliente`

## Tablas mencionadas estáticamente

`D_FACTURAF`, `P_CLIENTE`

## Métodos

- `onCreate` — línea 54.
- `consFinal` — línea 98.
- `clienteNIT` — línea 120.
- `buscarCliente` — línea 176.
- `setHandlers` — línea 182.
- `procesaCF` — línea 217.
- `correctoNIT` — línea 271.
- `procesaNIT` — línea 291.
- `purgeNIT` — línea 397.
- `cargaCliente` — línea 428.
- `showCliente` — línea 436.
- `guardaDatos` — línea 485.
- `consultaNITInfile` — línea 523.
- `onResponse` — línea 551.
- `onErrorResponse` — línea 567.
- `validaNIT` — línea 582.
- `validaNITOld` — línea 659.
- `validaNITHon` — línea 732.
- `validaNITSal` — línea 744.
- `existeCliente` — línea 799.
- `agregaCliente` — línea 842.
- `agregaClienteCF` — línea 916.
- `actualizaCliente` — línea 956.
- `nitnum` — línea 982.
- `limpiaCampos` — línea 1009.
- `cliente` — línea 1019.
- `pantallaHorizontal` — línea 1042.
- `onResume` — línea 1056.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

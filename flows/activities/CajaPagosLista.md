# CajaPagosLista

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/CajaPagosLista.java:37`; hereda `PBase`.

## Layouts candidatos

- `activity_caja_pagos_lista` — `app/src/main/java/com/dtsgt/mpos/CajaPagosLista.java:68`.

## Navegación candidata

- `CajaPagos` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaPagosLista.java:97`; condiciones en catálogo.
- `InvRecep` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaPagosLista.java:452`; condiciones en catálogo.
- `InvRecep` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/CajaPagosLista.java:525`; condiciones en catálogo.

## Estado global escrito

`codigo_proveedor`, `corelmov`, `nombre_proveedor`

## Tablas mencionadas estáticamente

`P_CAJAPAGOS`, `P_CONCEPTOPAGO`

## Métodos

- `onCreate` — línea 64.
- `nuevo` — línea 95.
- `setHandlers` — línea 103.
- `onItemClick` — línea 107.
- `listItems` — línea 132.
- `showDateDialog1` — línea 199.
- `showDateDialog2` — línea 208.
- `obtenerFecha` — línea 217.
- `onDateSet` — línea 220.
- `setFechaAct` — línea 273.
- `generarImpresion` — línea 297.
- `impresionEncabezado` — línea 339.
- `impresionDetalle` — línea 402.
- `msgAskImprimir` — línea 443.
- `onClick` — línea 450.
- `onClick` — línea 457.
- `onClick` — línea 461.
- `nombreOperador` — línea 474.
- `nombreTipo` — línea 484.
- `ajustaFormato` — línea 502.
- `onResume` — línea 515.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

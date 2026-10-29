# FinDia

Dominio: `cash-payments`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/FinDia.java:33`; hereda `PBase`.

## Layouts candidatos

- `activity_fin_dia` — `app/src/main/java/com/dtsgt/mpos/FinDia.java:55`.

## Navegación candidata

- `ComWS` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FinDia.java:177`; condiciones en catálogo.
- `PrintDialog` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FinDia.java:187`; condiciones en catálogo.
- `PrintDialog` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FinDia.java:662`; condiciones en catálogo.
- `Deposito` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FinDia.java:686`; condiciones en catálogo.
- `Reimpresion` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FinDia.java:697`; condiciones en catálogo.
- `ComWS` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FinDia.java:706`; condiciones en catálogo.
- `Menu` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FinDia.java:716`; condiciones en catálogo.
- `Clientes` (intent_candidate) — `app/src/main/java/com/dtsgt/mpos/FinDia.java:2485`; condiciones en catálogo.

## Estado global escrito

`autocom`, `corel_d_mov`, `devfindia`, `filtrocli`, `findiaactivo`, `modoadmin`, `prdlgmode`, `tipo`, `validimp`

## Tablas mencionadas estáticamente

`D_ATENCION`, `D_BONIF`, `D_BONIFFALT`, `D_BONIF_BARRA`, `D_BONIF_LOTES`, `D_BONIF_STOCK`, `D_CLICOORD`, `D_CLINUEVO`, `D_CLINUEVO_APR`, `D_COBRO`, `D_COBROD`, `D_COBROP`, `D_CXC`, `D_CXCD`, `D_DEPOS`, `D_DEPOSD`, `D_FACTURA`, `D_FACTURAD`, `D_FACTURAD_LOTES`, `D_FACTURAF`, `D_FACTURAP`, `D_FACTURA_BARRA`, `D_FACTURA_STOCK`, `D_MOV`, `D_MOVD`, `D_MOVDB`, `D_MOVDCAN`, `D_MOVDPALLET`, `D_NOTACRED`, `D_NOTACREDD`, `D_PEDIDO`, `D_PEDIDOD`, `D_REL_PROD_BON`, `D_REPFINDIA`, `D_SOLICINV`, `D_SOLICINVD`, `D_STOCKB_DEV`, `FINDIA`, `P_CLIENTE`, `P_COREL`, `P_PRODUCTO`, `P_STOCK`, `P_SUCURSAL`

## Métodos

- `onCreate` — línea 52.
- `run` — línea 92.
- `iniciaCierre` — línea 103.
- `startFDD` — línea 122.
- `run` — línea 184.
- `completeProcess` — línea 204.
- `buildReports` — línea 424.
- `Inserta_Enc_D_Mov` — línea 480.
- `validaFinDia` — línea 522.
- `validaPagosPend` — línea 626.
- `imprimeCierreZ` — línea 646.
- `run` — línea 660.
- `ActivityDeposito` — línea 684.
- `ActivityImpresion` — línea 694.
- `ActivityComunicacion` — línea 704.
- `ActivityMenu` — línea 714.
- `repProductos` — línea 729.
- `repFacturas` — línea 795.
- `repFacturasCredito` — línea 850.
- `repPedidos` — línea 912.
- `repTotales` — línea 967.
- `repDevolTotal` — línea 1045.
- `repEstadoMalo` — línea 1120.
- `buildReportsTOL` — línea 1215.
- `repFacturasTol` — línea 1288.
- `repPedidosTol` — línea 1438.
- `repCobrosTol` — línea 1588.
- `repNotasCreditoTol` — línea 1647.
- `repTotalesTol` — línea 1752.
- `FacturasCredito` — línea 1883.
- `FacturasContado` — línea 1911.
- `FacturasAnuladas` — línea 1939.
- `TotalFacturas` — línea 1964.
- `TotRecibos` — línea 1990.
- `RecibosAnulados` — línea 2016.
- `NotasCredito` — línea 2042.
- `NotasCreditoAnuladas` — línea 2068.
- `TotNotaC_Credito` — línea 2094.
- `TotNotaC_Contado` — línea 2122.
- `TotalCredito2` — línea 2149.
- `TotalEfectivo2` — línea 2177.
- `TotalRecibos` — línea 2202.
- `msgAskDeposito` — línea 2231.
- `onClick` — línea 2240.
- `onClick` — línea 2246.
- `msgAskImpresionDeposito` — línea 2258.
- `onClick` — línea 2267.
- `onClick` — línea 2273.
- `msgAskComunicacion` — línea 2283.
- `onClick` — línea 2292.
- `onClick` — línea 2298.
- `msgAskGeneraCierreZ` — línea 2308.
- `onClick` — línea 2317.
- `onClick` — línea 2333.
- `msgAskCierreIncompleto` — línea 2346.
- `onClick` — línea 2355.
- `onClick` — línea 2361.
- `msgAsk` — línea 2373.
- `onClick` — línea 2382.
- `onClick` — línea 2388.
- `msgAskFinDiaTrue` — línea 2400.
- `onClick` — línea 2406.
- `onClick` — línea 2413.
- `msgAsk2` — línea 2422.
- `onClick` — línea 2430.
- `onClick` — línea 2436.
- `msgAskDevInventario` — línea 2447.
- `msgExit` — línea 2458.
- `onClick` — línea 2465.
- `msgPendPago` — línea 2477.
- `onClick` — línea 2483.
- `msgAskFlag` — línea 2496.
- `onClick` — línea 2504.
- `onClick` — línea 2510.
- `Tiene_Inventario_Devolucion` — línea 2526.
- `Ya_Realizo_Devolucion` — línea 2576.
- `yaInicioFinDia` — línea 2619.
- `totRecibos` — línea 2645.
- `totDeposito` — línea 2673.
- `detVentas` — línea 2698.
- `detRecibos` — línea 2748.
- `setFactCor` — línea 2793.
- `delPrintFiles` — línea 2816.
- `onBackPressed` — línea 2832.
- `onResume` — línea 2837.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

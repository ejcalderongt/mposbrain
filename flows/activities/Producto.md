# Producto

Dominio: `support-catalogs`. Cobertura: **inventariado estático; no observado**.

## Evidencia

- `app/src/main/java/com/dtsgt/mpos/Producto.java:24`; hereda `PBase`.

## Layouts candidatos

- `activity_producto` — `app/src/main/java/com/dtsgt/mpos/Producto.java:47`.

## Navegación candidata


## Estado global escrito

`costo`, `gstr`, `linea_sel`, `pprodname`, `prodcod`, `prodtipo`, `um`

## Tablas mencionadas estáticamente

`P_FACTORCONV`, `P_LINEA`, `P_PRODPRECIO`, `P_PRODUCTO`, `P_STOCK`, `P_STOCK_ALMACEN`

## Métodos

- `onCreate` — línea 43.
- `porCodigo` — línea 86.
- `porNombre` — línea 96.
- `setHandlers` — línea 106.
- `afterTextChanged` — línea 173.
- `beforeTextChanged` — línea 175.
- `onTextChanged` — línea 177.
- `onItemSelected` — línea 189.
- `onNothingSelected` — línea 213.
- `listItems` — línea 230.
- `appProd` — línea 357.
- `getDisp` — línea 370.
- `fillSpinner` — línea 507.
- `ltrim` — línea 606.
- `prodBarra` — línea 625.
- `limpiaFiltro` — línea 634.
- `prodPrecioBase` — línea 643.
- `onResume` — línea 671.

## Para acreditar aprendizaje operativo

Registrar rol, país, parámetros, precondiciones, acción, transición, resultado y evidencia sanitizada. No convertir esta lista estática en una afirmación de pruebas end-to-end.

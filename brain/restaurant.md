# Restaurante: recorrido prioritario

Estado: mapa de código bd94c90c, recorrido dinámico completo pendiente. Los nombres de actividades no son necesariamente los textos que ve el operador.

| Etapa | Componentes / evidencia | Estado que se debe observar |
|---|---|---|
| Acceso | MainActivity, Menu, Venta; Menu.valmodulo/valmenu | Empresa/país, caja/ruta, rol, permisos, peRest |
| Mesas | SalonMesas.FbMesaAbierta → SalonOrden (645); FbMesaComensales → Comensales (669) | Sala, mesa, mesero, comensales, cuenta y correlativo |
| Pedido | SalonOrden, Producto, OrdenMenu; SalonOrden.finalizarOrden (2033) → FacturaRes (2069) | Líneas, cantidades, precios, descuentos, envío de comanda |
| Precuenta | FacturaRes; activity_factura_res_precue | Modelo, porcentaje/monto, exclusiones y elección de impresión |
| Caja | SalonCajaIngreso/ValidaClave → ResCaja; ResCaja.crearVenta/menuVenta | Cuenta actualizada, venta temporal y avisos de pago |
| Cobro | FacturaRes.paySelect → Pago (642); payCard → PagoTarjeta (693) | Medios, importes, saldo, propina persistida y transacción |
| Documento | FacturaRes.finishOrder/impresionDocumento; clsDocCuenta/clsDocument | Resultado de generación, archivo nuevo y despacho |
| Cierre | CierreInicio, FinDia y opciones de Menu | Apertura/cierre, conciliación, correlativos y envíos |

SalonOrden.estadoCuenta publica estado de cuenta mediante su adaptador Firebase. ResCaja consulta actualización y puede mostrar “La cuenta no está actualizada”. ResCaja también elimina entradas de su lista Firebase, con aclaración de que no borra artículos ni cuenta. No probar esas acciones contra datos reales por tratarse de una pantalla de consulta.

FacturaRes puede iniciar WSEnv, srvCommit y rutas FEL según configuración. El cobro no se considera offline sólo por haber abierto la pantalla desde una base local. Para explorar escrituras sin afectar al servidor, usar variante sin INTERNET y fixture sintética; registrar qué dependencias remotas impiden completar el recorrido.

## Huella por transición

Registrar pantalla origen/destino, ID de acción, configuración relevante, rol, identificadores sintéticos de mesa/cuenta, estado global antes/después, tablas afectadas, llamadas de integración y resultado. Los datos reales y textos libres permanecen privados. La versión pública contiene estructura y cantidades no sensibles, nunca contraseña ni nombres de clientes.

## Matriz mínima de regresión

- Mesa nueva y existente; una y varias cuentas; regreso y reapertura.
- Pedido simple, cambios de cantidad, anulación de línea, traslado/división si el rol lo permite.
- Precuenta con/sin/con propina, cancelación de diálogo, reapertura, rotación y reinicio.
- Propina fija/variable; descuento cero/positivo; exclusiones llevar/domicilio/sin_propina.
- Impresión correcta, fallo de generación, fallo de guardado y archivo anterior existente.
- Cobro efectivo y mixto; cancelación/reintento; saldo cero y pendiente.
- Cierre con y sin pendientes; conciliación con documentos realmente emitidos.

Cada fila necesita fixture, precondición y aserción. Esta matriz es un plan de cobertura; no una declaración de que los casos ya pasaron.

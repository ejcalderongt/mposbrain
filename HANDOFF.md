# Handoff operativo

## Contexto confirmado

Incidente: una misma cuenta puede mostrar o imprimir importes distintos de propina. El cliente opera en Honduras. El usuario confirmó que la precuenta pasa por footerBaseGUA(). Quiere reproducir el fallo al retirar cuatro blindajes, no sólo acumular logs.

Prioridad confirmada por el usuario: restaurante completo, mesas → pedidos → precuenta → cobro → cierre.

Checkout habitual: C:/Users/yejc2/source/repos/mPos2025, rama dev626b_ejc. Brain: C:/Users/yejc2/source/repos/mpos-brain. El checkout tiene ajustes locales de Gradle/JDK del usuario; deben preservarse.

Baselines: b12b47665a28bafb57f4bb85de989b31b0b2613b original; c21e92ec diagnóstico previo a blindajes; bd94c90c blindajes y menú de diagnóstico. Los laboratorios usan commits, no copian cambios sin guardar.

## Sesión actual

Inventario AST Java y XML generado sin copiar textos de código ni literales sensibles. Consultar catalog/scan-summary.json para cifras y huella. Todas las actividades detectadas tienen ficha estática en flows/activities. Los flujos requieren validar configuración, rol y ejecución.

Entorno local: .venv con tree-sitter 0.25.2 y tree-sitter-java 0.23.5. La versión 0.26.0 produjo una excepción nativa al escanear este corpus; el lock conserva la versión que completó el análisis.

Índice adicional de configuración: 123 bloques/110 IDs de P_PARAMEXT en AppMethods, con escrituras de cuerpo/catch y presencia QA sin valores. Ver brain/configuration.md. MantConfig activa 118; MantConfigRes no equivale a esa activación. CI instala el parser fijado antes de probar estos extractores.

Laboratorio offline: AVD mPos_Brain_Lab_10, puerto 5580, 1280x800, 10 pulgadas. Clones ignorados: .local/workspaces/guarded, rollback y qa. Los dos primeros eliminan INTERNET del manifest; QA conserva red para el alta autorizada.

QA de recepción: AVD mPos_Brain_QA_10_API35, puerto 5584, imagen Google APIs API 35. El primer AVD QA con API 37.2 falló antes de ejecutar mPos. Ver evidence/lab-environment.md. Nunca limpiar datos después de recibir una base sin conservar copia privada.

El usuario enseñó el alta: base vacía abre Comunicación; empresa y clave permiten recibir configuración/catálogos desde su servicio AWS QA. Los insumos están exclusivamente en .local/qa-input.json. No pedirlos otra vez ni copiarlos a documentación pública.

## Pendientes que impiden declarar el objetivo completo

1. Contratos Android A/B completados: guarded 7/7; rollback cinco regresiones esperadas y dos controles aprobados. evidence/experiments/comparison.json registra propina 0 y despacho del archivo previo en fixtures sintéticas. Falta reproducción de UI completa e impresora física.
2. Tres cargas QA aprobadas: 33, 32 y 29 huellas, con snapshots consistentes. La segunda configuró la caja mediante controles reales de ConfigCaja, recibió 118 y cambió peRest a true; la tercera recibió 1 sala y 133 mesas. Evidencia: qa-stage2.json y qa-stage3.json. No repetir cargas por inercia. Perfil autorizado en .local/qa-profile.json. El usuario también indicó mesero, gerente y cajero; son selectores que corresponden a CLAVE en VENDEDORES. Se resolvieron candidatos activos de la ruta por NIVEL y se guardaron en .local/qa-selected-operators.json. No pedir de nuevo esos datos ni publicarlos.
3. Recorrer restaurante, mesas, cuentas, precuenta, cobro e impresión con una copia privada offline; delimitar acciones que escriben en servidor.
4. Skill mpos-operational-agent instalada y validada; narrativas iniciales, analizador de trazas y matriz de cobertura disponibles. Completar narrativas con las observaciones de restaurante que aún faltan.
5. Repositorio ya tiene commits locales y controles aprobados. No hay repositorio GitHub elegido ni publicación realizada.

Backend local verificado: Firebase RTDB demo-mpos-brain en loopback 19000, con roundtrip SDK Android y eliminación de la sonda aprobados. AVD dedicado mPos_Brain_Flow_10_API35, serial emulator-5586. El gate bloquea salida IPv4/IPv6 de UID de aplicaciones y permite loopback; se verifica antes de cada receta contra boot, APK y reglas exactas. No asumir que sigue activo tras reiniciar. Evidencias en evidence/firebase. La variante de flujo conserva INTERNET para el SDK, a diferencia de los contratos offline; su aislamiento depende del gate obligatorio. No desplegar las reglas locales a Firebase real.

Accesos nativos aprobados para mesero, gerente y cajero (evidence/auth), usando selección y teclado reales de Main. Las claves quedan privadas. NIVEL observado: mesero 4, gerente 3, cajero 1; no confundir este último con la autorización de caja de restaurante NIVEL 5. Ruta observada: Main → Menu → Venta → ValidaClave → ResMesero. peSalon=false, peNoCierre=true y ambos PIN subordinados desactivados. Ver brain/restaurant.md.

Punto exacto de continuación: waiter_enter_tables llega a ResMesero pero tiene un diálogo de grupos encima; NO prueba mesas visibles. La base recibida tiene cero P_MESERO_GRUPO para el mesero seleccionado. showGrupoMenu abre showGrupoChecks cuando falta asignación y después muestra el selector; hace falta recorrer Configurar → asignar grupo → Aplicar mediante controles reales. scripts/flow_choices.py se detiene deliberadamente por ausencia de grupo; además las mesas usan nombres alfanuméricos, no sólo números. Corregir la selección de fixture y completar asignación nativa antes de ejecutar waiter-open-table.json. Esa receta todavía NO pasó y no existe evidencia de llegada a Comensales. No insertar asignaciones por SQL para saltarse este aprendizaje.

No confundir pruebas sintéticas de candidatos con la causa histórica del cliente. La validación de impresora física y configuración completa sigue siendo necesaria.

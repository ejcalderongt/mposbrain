# Handoff operativo

## Contexto confirmado

Incidente: una misma cuenta puede mostrar o imprimir importes distintos de propina. El cliente opera en Honduras. El usuario confirmó que la precuenta pasa por footerBaseGUA(). Quiere reproducir el fallo al retirar cuatro blindajes, no sólo acumular logs.

Prioridad confirmada por el usuario: restaurante completo, mesas → pedidos → precuenta → cobro → cierre.

Checkout habitual: C:/Users/yejc2/source/repos/mPos2025, rama dev626b_ejc. Brain: C:/Users/yejc2/source/repos/mpos-brain. El checkout tiene ajustes locales de Gradle/JDK del usuario; deben preservarse.

Baselines: b12b47665a28bafb57f4bb85de989b31b0b2613b original; c21e92ec diagnóstico previo a blindajes; bd94c90c blindajes y menú de diagnóstico. Los laboratorios usan commits, no copian cambios sin guardar.

## Sesión actual

Inventario AST Java y XML generado sin copiar textos de código ni literales sensibles. Consultar catalog/scan-summary.json para cifras y huella. Todas las actividades detectadas tienen ficha estática en flows/activities. Los flujos requieren validar configuración, rol y ejecución.

Entorno local: .venv con tree-sitter 0.25.2 y tree-sitter-java 0.23.5. La versión 0.26.0 produjo una excepción nativa al escanear este corpus; el lock conserva la versión que completó el análisis.

Laboratorio offline: AVD mPos_Brain_Lab_10, puerto 5580, 1280x800, 10 pulgadas. Clones ignorados: .local/workspaces/guarded, rollback y qa. Los dos primeros eliminan INTERNET del manifest; QA conserva red para el alta autorizada.

QA de recepción: AVD mPos_Brain_QA_10_API35, puerto 5584, imagen Google APIs API 35. El primer AVD QA con API 37.2 falló antes de ejecutar mPos. Ver evidence/lab-environment.md. Nunca limpiar datos después de recibir una base sin conservar copia privada.

El usuario enseñó el alta: base vacía abre Comunicación; empresa y clave permiten recibir configuración/catálogos desde su servicio AWS QA. Los insumos están exclusivamente en .local/qa-input.json. No pedirlos otra vez ni copiarlos a documentación pública.

## Pendientes que impiden declarar el objetivo completo

1. Contratos Android A/B completados: guarded 7/7; rollback cinco regresiones esperadas y dos controles aprobados. evidence/experiments/comparison.json registra propina 0 y despacho del archivo previo en fixtures sintéticas. Falta reproducción de UI completa e impresora física.
2. Ejecutar el alta real y aprender selección de sucursal/caja/usuario según respuestas del servicio.
3. Recorrer restaurante, mesas, cuentas, precuenta, cobro e impresión con una copia privada offline; delimitar acciones que escriben en servidor.
4. Completar narrativas funcionales, matriz de cobertura dinámica, validación del brain y skill instalada.
5. Revisar seguridad y crear commit local. No hay repositorio GitHub elegido ni publicación realizada.

No confundir pruebas sintéticas de candidatos con la causa histórica del cliente. La validación de impresora física y configuración completa sigue siendo necesaria.

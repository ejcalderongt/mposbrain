# Backend local para recorridos de restaurante

Preparación en curso; no es todavía evidencia de recorridos aprobados. Se usa el proyecto ficticio demo-mpos-brain y un emulador Realtime Database ligado sólo a 127.0.0.1:19000. Las reglas abiertas son exclusivamente para ese proceso local; no son reglas de despliegue ni deben publicarse en un proyecto remoto.

Actualización observada: evidence/firebase contiene roundtrip host y SDK Android aprobados, sonda eliminada y conexión externa bloqueada. evidence/auth prueba los tres accesos nativos. evidence/flows prueba entrada a Venta y llegada a ResMesero con diálogo de grupos. Todavía no hay evidencia de pedido, precuenta, cobro ni cierre completos. scripts/flow_network_gate.py establece el aislamiento exclusivamente en el AVD de flujo y scripts/flow_fixture.py lo verifica antes de importar o ejecutar recetas. La verificación depende del boot y del APK; repetirla tras cambios, sin asumir que una ejecución anterior basta.

La CLI standalone oficial se instala en .local/tools con scripts/install_firebase_tools.py y digest SHA-256 fijado. No se necesita iniciar sesión para el proyecto demo ni consultar proyectos del usuario. Configuración y puertos están separados de los defaults para evitar colisiones con otros trabajos.

Antes de ejecutar flujos que escriben, el clon de aplicación debe apuntar al backend local y el AVD debe bloquear acceso externo. El APK de recepción QA queda separado. La conectividad local por ADB reverse debe probarse, y un intento de conexión externa debe fallar, antes de admitir ventas/cobros/cierres sintéticos.

No basta cambiar la URL por convención. Se deben verificar SDK configurado, namespace, destino observado y ausencia de escrituras en el backend real. Hasta que esos controles pasen no se ejecutan flujos de escritura.

Referencias oficiales: [Emulator Suite](https://firebase.google.com/docs/emulator-suite/install_and_configure), [conectar Android a RTDB local](https://firebase.google.com/docs/emulator-suite/connect_rtdb), [CLI](https://firebase.google.com/docs/cli). El código actual fbBase usa FirebaseDatabase.getInstance(), lo que permite redirigir la instancia predeterminada antes de crear referencias. Esto debe aplicarse exclusivamente al clon de laboratorio.

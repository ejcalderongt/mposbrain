# Auditoría de alcance

Estado: objetivo activo; no está completo. Esta matriz mantiene la meta original y distingue scaffolding, pruebas de componentes y recorridos operativos.

| Requisito | Evidencia actual | Estado / siguiente prueba |
|---|---|---|
| Repo separado y versionado | Raíz Git independiente; commits, AGENTS y HANDOFF | Implementado; verificar limpieza al entregar cada avance |
| Capas y aprendizaje continuo | brain/INDEX, narrativas, catálogos, learning y templates | Estructura instalada; incorporar cada flujo observado |
| Deep scan | AST/XML, actividades, estado, SQL, configuración y eventos | Cobertura sintáctica; semántica de negocio por completar |
| Alta real | Tres cargas Android aprobadas; perfil, parámetro y mesas observados | Observado, con entrada directa del test a ConfigCaja/WSRec |
| Mesas/pedidos/precuenta/cobro/cierre | Matriz y código candidatos; catálogo de mesas recibido | Faltan recorridos y aserciones de estado/persistencia |
| Fingerprints finos | Lifecycle global, snapshots de propina, 94 huellas del alta | Falta cobertura de transiciones y estados del restaurante |
| Pruebas/diagnóstico de errores | A/B Android y controles del brain; fallos de laboratorio separados | Falta regresión completa del restaurante y prueba de recuperación |
| Agente funcional | Skill instalada y validada; playbook y herramientas | Debe demostrar ejecutar, diagnosticar y validar flujos aún pendientes |
| Retirar cuatro blindajes y reproducir cero | Cinco contratos regresan sin blindajes, pasan con ellos | Confirmado a nivel componente/bloques; falta secuencia UI de reproducción |
| Preservar checkout del usuario | Experimentos en clones privados; cambios Gradle/JDK conservados | Invariante que se comprueba antes de cada entrega |
| GitHub | Repo local con CI y control de contenido público | Preparado localmente; destino/publicación aún no definidos |

La impresora física no está conectada: se conserva como límite de validación, sin confundir generación/despacho con papel emitido. No usar esa limitación para omitir pruebas de UI o persistencia que sí pueden realizarse en el laboratorio.

No se considera completado el objetivo por pasar el A/B ni por tener un índice de todas las actividades. La siguiente fase requiere backend local probado, aislamiento de salida y operadores autorizados antes de hacer escrituras sintéticas.

# mPos brain

Conocimiento operativo independiente del código de mPos. Comienza en [HANDOFF.md](HANDOFF.md) y [brain/INDEX.md](brain/INDEX.md).

Este repositorio distingue hechos leídos en código, observaciones ejecutadas e hipótesis. Los índices estáticos no demuestran que una pantalla sea accesible para un rol o una empresa determinados. No contiene copias de bases, credenciales, datos de clientes ni APK.

## Uso

1. Leer AGENTS.md y HANDOFF.md.
2. Consultar catalog/scan-summary.json y comprobar el commit del código antes de confiar en líneas o flujos.
3. Buscar la actividad en flows/INDEX.md y cruzar navegación, estado global, SQL e impresión.
4. Reproducir en un AVD dedicado. Registrar evidencia nueva y sus límites.
5. Actualizar hechos e hipótesis; ejecutar las validaciones antes de hacer commit.

El escáner requiere Python y las versiones de requirements-scanner.lock. Los laboratorios se preparan con scripts/lab_prepare.py; sus clones y resultados privados viven bajo .local, excluido de Git. Consultar experiments/propina/README.md antes de ejecutarlos.

Estado: inventario estático generado y contraste Android de propina confirmado: siete contratos aprobados con blindajes, cinco regresiones reproducidas sin ellos y dos controles aprobados en ambas versiones. Ver evidence/experiments/RESULTS.md. El aprendizaje dinámico del restaurante completo sigue en construcción. La publicación en GitHub requiere revisar el contenido y elegir un repositorio de destino.

El alta QA también pasó y tiene 33 huellas estructurales y esquema SQLite verificado. Falta confirmar el perfil de Restaurante: QA no envió el parámetro que habilita ese módulo. Consultar brain/onboarding.md y HANDOFF.md antes del siguiente recorrido.

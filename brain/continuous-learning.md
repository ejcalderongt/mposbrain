# Ciclo de aprendizaje

La unidad de aprendizaje es una transición verificable o una regla de negocio con contraejemplos. Cada incidente añade conocimiento; no debe terminar únicamente en una conversación.

1. Orientar: comprobar commit, ruta, configuración y cobertura existente.
2. Formular: síntoma, hipótesis y evidencia que podría refutarla.
3. Reproducir: fixture privada/sintética, precondición, acción y aserción.
4. Correlacionar: pantalla, estado global, SQL, integración, archivo e impresión.
5. Corregir: cambio mínimo y trazas suficientes para detectar coincidencia.
6. Contrastar: mismo escenario antes/después y controles vecinos.
7. Consolidar: actualizar narrativa funcional, evidencia, glosario, cobertura y handoff; añadir una entrada con templates/learning.md.

Si aparece una diferencia entre documentación y ejecución, conservar ambos con sus commits y registrar qué evidencia reemplaza la afirmación anterior. No borrar la incertidumbre convirtiendo una hipótesis en hecho.

El catálogo se regenera desde código. Las narrativas revisadas por humanos y las observaciones se mantienen fuera de los archivos generados. El validador detecta drift por hashes contra el checkout local. CI verifica integridad pública sin necesitar acceso al código privado ni a credenciales.

La skill instalada se versiona en agent/skills/mpos-operational-agent. Puede usarse desde un agente para todo el recorrido o desde agentes especializados en navegación, datos e impresión; todos deben respetar el mismo contrato de evidencia. La instalación de una skill no acredita capacidad de completar flujos que aún no fueron observados.

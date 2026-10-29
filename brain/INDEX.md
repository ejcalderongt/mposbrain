# Capas del conocimiento

| Capa | Entrada | Qué responde |
|---|---|---|
| Operación | onboarding.md | Cómo se inicia y recibe configuración |
| Arquitectura | architecture.md | Componentes, estado compartido e integraciones |
| Restaurante | restaurant.md | Recorrido prioritario y matriz de validación |
| Conceptos | glossary.md | Nombres ambiguos y unidades que deben seguirse |
| Configuración | configuration.md | Parámetros, banderas, defaults y presencia QA |
| Navegación | ../flows/INDEX.md | Actividades, layouts e Intents candidatos |
| Estado | ../catalog/global_state.jsonl | Quién lee/escribe estado compartido |
| Datos | ../catalog/sql_access.jsonl, schema_candidates.jsonl | Operaciones y tablas inferidas de código |
| Persistencia de restaurante | persistence.md | Handlers, unidades y registro de propina |
| Integraciones | ../catalog/wsdl-operations.json | Operaciones expuestas por WSDL QA |
| Incidentes | propina.md | Candidatos, mecanismos y pruebas |
| Evidencia | ../evidence/ | Resultados sanitizados reproducibles |
| Telemetría | telemetry.md | Extracción, correlación y límites de las trazas |
| Cobertura | coverage.md | Qué está probado y qué sigue pendiente |
| Auditoría de alcance | completion-audit.md | Requisitos originales y evidencia que falta |
| Aprendizaje continuo | continuous-learning.md | Ciclo de incorporación y revisión |
| Aprendizaje | ../templates/learning.md | Cómo incorporar evidencia nueva |
| Bitácora | ../learning/2026-10-29.md | Hechos incorporados y comprobaciones pendientes |

Los inventarios generados por dominio se encuentran en generated. La clasificación por nombre de archivo ayuda a buscar; no establece reglas de negocio. Los esquemas SQL son candidatos estáticos, no el esquema efectivo de una base sincronizada.

# Capas del conocimiento

| Capa | Entrada | Qué responde |
|---|---|---|
| Operación | onboarding.md | Cómo se inicia y recibe configuración |
| Restaurante | restaurant.md | Recorrido prioritario y matriz de validación |
| Conceptos | glossary.md | Nombres ambiguos y unidades que deben seguirse |
| Navegación | ../flows/INDEX.md | Actividades, layouts e Intents candidatos |
| Estado | ../catalog/global_state.jsonl | Quién lee/escribe estado compartido |
| Datos | ../catalog/sql_access.jsonl, schema_candidates.jsonl | Operaciones y tablas inferidas de código |
| Integraciones | ../catalog/wsdl-operations.json | Operaciones expuestas por WSDL QA |
| Incidentes | propina.md | Candidatos, mecanismos y pruebas |
| Evidencia | ../evidence/ | Resultados sanitizados reproducibles |
| Aprendizaje | ../templates/learning.md | Cómo incorporar evidencia nueva |

Los inventarios generados por dominio se encuentran en generated. La clasificación por nombre de archivo ayuda a buscar; no establece reglas de negocio. Los esquemas SQL son candidatos estáticos, no el esquema efectivo de una base sincronizada.

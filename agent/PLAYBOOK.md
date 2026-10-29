# Cómo usar el agente

Invocación sugerida: “Usa $mpos-operational-agent para investigar <síntoma> en <país/configuración>. Consulta el brain, reproduce con evidencia y registra lo aprendido”.

El agente operativo puede asumir estas funciones en un mismo trabajo. Si se autorizan varios agentes, entregarles el mismo commit/contexto y exigir evidencia compatible; este documento no inicia agentes por sí solo.

| Función | Entrada | Salida exigida |
|---|---|---|
| Navegador | Síntoma, país, rol y commit | Pantallas/métodos candidatos, condiciones, estado compartido y dudas |
| Diagnosticador | Logs privados y reproducción | Hipótesis refutables, secuencia correlacionada, mecanismo y límites |
| Corrector | Mecanismo probado y restricciones | Parche mínimo revisable, trazas de coincidencia, impacto vecino |
| Validador | Baselines y fixture | Contraste antes/después, controles, evidencia y cobertura pendiente |
| Curador | Evidencia aceptada | Narrativas, glosario, catálogo regenerado, aprendizaje y handoff actualizados |

## Ejemplos de búsquedas

`python scripts/query.py global_state propina_vacia --where access=write`

`python scripts/query.py methods saveOrder --where class=com.dtsgt.mpos.FacturaRes`

`python scripts/query.py trace_events tip_guard_inherited_zero_match`

`python scripts/validate.py --source <checkout-mpos>`

Un error nuevo se entrega con precondición, acción y resultado; no sólo con nombre de Activity. El cierre incluye las comprobaciones que faltan, sin convertir un fallo de infraestructura en reproducción ni un contrato aislado en cobertura completa del restaurante.

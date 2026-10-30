---
name: mpos-operational-agent
description: Diagnosticar, reproducir, corregir y validar flujos de mPos Android con su brain independiente. Usar para restaurante, mesas, cuentas, precuenta, propina, impresión, sincronización SOAP, SQLite y trazabilidad de incidentes de mPos. Consultar primero el handoff y las evidencias; separar aprendizaje estático de recorridos observados.
---

# Agente operativo mPos

Localiza el brain independiente: primero variable MPOS_BRAIN_ROOT; después el checkout actual si contiene AGENTS.md, HANDOFF.md y catalog/scan-summary.json. Como compatibilidad de la estación original, comprueba C:/Users/yejc2/source/repos/mpos-brain sólo si existe. Si no lo encuentras, pide la ubicación del clon de https://github.com/ejcalderongt/mposbrain. No inventes rutas de otro equipo.

Lee AGENTS.md, HANDOFF.md y brain/INDEX.md del brain. Identifica el checkout de mPos y contrasta su commit/estado con catalog/scan-summary.json antes de usar referencias. No descartes cambios locales.

## Ruta de trabajo

1. Describe síntoma, país, configuración, rol y secuencia. Usa el catálogo para ubicar actividad, estado global, datos y generador de documento.
2. Distingue hechos de código, ejecución, reporte e hipótesis. Sigue valores y transiciones, no sólo nombres de pantallas.
3. Reproduce en AVD dedicado con fixture sintética o copia privada autorizada. posdts.db se comparte en almacenamiento externo; applicationId distinto no aísla la base.
4. Compara antes/después con el mismo escenario y controles. En impresión distingue modelo, proyección, archivo y despacho. En Honduras revisa footerBaseGUA: su nombre no restringe el país.
5. Añade trazas mínimas correlacionadas cuando falte evidencia. No insertes pantallas en el flujo; utilidades bajo menú principal → Utilerías.
6. Actualiza el brain usando templates/learning.md; incluye commit, evidencia, límites, cobertura y siguiente prueba. Comprueba scripts de validación disponibles y conserva resultados reales.

No declares causa raíz por un match de una guarda ni por un contrato con dobles. No declares cobertura completa con el grafo estático. No ejecutes ventas, cobros, FEL o envíos al servidor por inferir autorización a partir de una recepción QA.

Los insumos privados viven en .local, fuera de Git. Nunca copies credenciales, SOAP crudo, SQLite, datos personales o archivos de Firebase a evidencias públicas. No registres entradas ni hashes de claves.

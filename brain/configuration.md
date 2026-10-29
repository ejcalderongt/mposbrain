# Parámetros que determinan los flujos

Proveniencia: AppMethods.java de bd94c90c; hashes y conteos en catalog/config-summary.json. scripts/config_index.py mapea 123 bloques de consulta y 110 IDs literales de P_PARAMEXT a escrituras globales del mismo try. Es un índice de candidatos, no un motor de ejecución ni un análisis completo de flujo de datos.

El valor recibido no basta para predecir la pantalla: hay conversiones, validación, excepciones, valores por defecto y otras banderas. Un parámetro ausente puede ser normal. No interpretar el conteo de ausentes como cantidad de errores.

| Parámetro | Campo | Comportamiento verificado en código | Presencia QA |
|---|---|---|---|
| 117 | pePropinaFija | S activa; catch toma true | Presente, S verificado por lista permitida |
| 118 | peRest | S activa; catch toma false | Ausente en la recepción inicial |
| 120 | pePropinaPerc | Convierte a double; fuera de 0–99 pasa a cero; catch cero | Presente, 10 verificado |
| 207 | pePreguntaPropina | S activa; catch toma false | Presente, S verificado |

Consultas rápidas: `python scripts/query.py config_params peRest` y `python scripts/query.py config_params pePropinaPerc`. Cada escritura distingue cuerpo/catch, línea y tipo de asignación. Sólo se exportan constantes booleanas y numéricas; nunca strings de configuración.

catalog/qa-config-presence.json cruza los IDs con el snapshot privado: 39 presentes y 71 ausentes entre los 110 IDs detectados. No hubo duplicados entre esos IDs en esta copia. El archivo publica presencia y cardinalidad, nunca valores. Para otras bases, duplicados con valores distintos requieren revisar la elección de la primera fila en las consultas sin orden explícito; no son una causa confirmada del incidente de propina.

## Restaurante durante el alta

WSRec consulta sala, mesa y grupo sólo con peRest activo. El primer despacho de una fase no acredita que se llamó a SOAP: existe callEmptyMethod para las ramas deshabilitadas. Por eso la recepción puede aprobar y dejar P_RES_SALA/P_RES_MESA vacíos.

MantConfig.updateItem escribe 118 con el rótulo “Modulo restaurante”. MantConfigRes modifica otras opciones del restaurante, pero su nombre no significa que active 118. No confundir ambas pantallas al guiar al operador. Confirmar perfil esperado, acceder por la ruta permitida y observar recarga de AppMethods antes de acreditar el flujo habilitado.

El usuario aclaró el alta real de tres cargas: empresa → perfil de ruta → mesas. En ese contexto, la ausencia de 118 tras la primera carga es esperable; no corregirla insertando el parámetro manualmente. Completar las cargas con la caja autorizada y observar cuándo cambia peRest.

## Regeneración y límites

`python scripts/config_index.py --source <checkout> --database <snapshot-privado-en-.local>`

La extracción sólo cubre lookups literales de P_PARAMEXT en AppMethods. IDs dinámicos, consultas construidas fuera del bloque, setters indirectos y configuración de otras tablas requieren seguir sus llamadores. Si un try tiene varios IDs, no asignar automáticamente cada escritura a cada parámetro. Los valores de catch representan escrituras del código, no prueba de que el catch se ejecutó en la sesión.

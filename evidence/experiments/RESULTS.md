# Resultado A/B de propina

Ejecución real Android, 2026-10-29, fixture Honduras. Commits, fragmentos extraídos y SHA del APK en guarded.json y rollback.json. comparison.json se genera automáticamente y rechaza diferencias inesperadas o errores de infraestructura.

| Contrato | Sin blindajes | Con blindajes |
|---|---|---|
| Imprimir sin y luego con propina | Propina posterior 0 | Propina posterior 13.50 |
| Elegir con propina tras bandera heredada | Porcentaje 0 | Porcentaje 10 |
| Footer con propina variable positiva | Omite propina y total | Incluye ambos |
| Excepción de generación | Reporta éxito | Reporta fallo |
| Fallo de guardado con recibo anterior | Despacha archivo anterior | Bloquea despacho |
| Control propina fija | Aprueba | Aprueba |
| Control exclusión sin_propina | Aprueba | Aprueba |

La pregunta “¿puede reproducirse propina 0 al retirar los blindajes?” tiene respuesta afirmativa al nivel de estos componentes y bloques reales extraídos. No se ha acreditado todavía la secuencia completa de pantallas que lo activó en el cliente. La prueba de despacho antiguo también reproduce el patrón modelo actual sin propina / artefacto anterior con propina, con un driver de impresión sintético.

Los encabezados DB y la impresora son dobles, y el cálculo completo no se ejecuta en el probe de recuperación de porcentaje. Estas limitaciones son parte del resultado y no deben omitirse al comunicarlo.

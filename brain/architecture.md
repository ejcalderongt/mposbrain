# Arquitectura operativa inicial

Proveniencia: código bd94c90c y catálogo generado; no es una arquitectura ideal propuesta.

El proyecto Gradle contiene el módulo :app. FacturaRes es una Activity, aunque operativamente se le llame módulo. La mayor parte del negocio vive en actividades Java que heredan PBase, apoyadas por AppMethods, appGlobals, clases de documento, adaptadores y clases de acceso a datos.

PBase.InitBase abre BaseDatos, obtiene appGlobals e instancia AppMethods y utilidades. appGlobals comparte estado mutable entre actividades; cambiar pantallas no reinicializa automáticamente sus banderas. BaseDatos utiliza posdts.db en almacenamiento externo. Las actualizaciones estructurales pasan por BaseDatosVersion.

La integración combina SOAP ASMX, llamadas HTTP/WebAPI, Firebase y servicios Android. No asumir que todo pasa por el endpoint de Comunicación ni que una pantalla con SQLite sea offline. Las clases bajo firebase, webapi y servicios deben entrar al análisis de impacto.

La impresión separa composición de documento, guardado y despacho a driver/aplicación externa. Existen SDK y controladores específicos. Comprobar el archivo efectivamente generado y el resultado del driver; el retorno de una llamada no acredita que salió papel.

La ruta fiscal depende de país y configuración. Las precuentas usan una implementación de footer compartida cuyo nombre Guatemala resulta engañoso en Honduras. Evitar inferir alcance por nombres de clases o métodos.

La configuración recibida, los permisos y las banderas de operación alteran rutas. Para reproducir un error hacen falta tanto versión del código como perfil de configuración, estado de sesión y secuencia de acciones. El catálogo AST organiza sitios y dependencias candidatas; no resuelve todo el despacho ni reemplaza ejecución.

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

Estado: inventario estático generado y contraste Android de propina confirmado: siete contratos aprobados con blindajes, cinco regresiones reproducidas sin ellos y dos controles aprobados en ambas versiones. Ver evidence/experiments/RESULTS.md. El aprendizaje dinámico del restaurante completo sigue en construcción. Repositorio compartido: https://github.com/ejcalderongt/mposbrain.

El alta QA de tres cargas pasó: empresa, perfil de ruta y mesas. Se conservaron 94 huellas estructurales entre las tres etapas, y la última recibió 1 sala y 133 mesas. Login, pedidos, precuenta, cobro y cierre todavía requieren sus recorridos aislados. Consultar brain/onboarding.md y HANDOFF.md antes de continuar.

## Instalación para otros usuarios

Clona el brain (el código de la aplicación mPos se obtiene por separado con sus permisos):

```powershell
git clone https://github.com/ejcalderongt/mposbrain.git mpos-brain
cd mpos-brain
$env:MPOS_BRAIN_ROOT = (Get-Location).Path
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-scanner.lock
```

Para consultar los catálogos no necesitas Android ni el código fuente:

```powershell
.\.venv\Scripts\python.exe scripts/query.py navigation ResMesero --limit 10
.\.venv\Scripts\python.exe scripts/validate.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe scripts/compare.py
```

Para instalar la skill en Codex, copia la carpeta `agent/skills/mpos-operational-agent` a la carpeta `skills` de tu instalación de Codex (habitualmente `~/.codex/skills`). Define `MPOS_BRAIN_ROOT` con la ruta de tu clon en el entorno desde el que inicias Codex. Lee también [agent/PLAYBOOK.md](agent/PLAYBOOK.md).

Las rutas de la estación original en HANDOFF y evidencias son referencias históricas. Cada usuario debe localizar su propio checkout de mPos y verificar el commit; el catálogo actual corresponde a `bd94c90c6b097887a1c3d75ef6f70351bd031921`. Los laboratorios requieren Android SDK, emulador, código fuente y configuración privada propia; consulta sus README antes de ejecutarlos. Clonar este repositorio no habilita acceso a servicios QA ni aporta credenciales, bases o APK.

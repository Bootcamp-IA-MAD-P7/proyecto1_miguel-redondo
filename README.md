# Proyecto 1 - Taximetro Digital F5

![Python](https://img.shields.io/badge/Python-3.11-3776AB)
![Estado](https://img.shields.io/badge/Estado-Entrega%20tecnica%20completada-2ea44f)
![Tests](https://img.shields.io/badge/Tests-14%20passed-2ea44f)
![CLI](https://img.shields.io/badge/CLI-Funcional-0969da)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-0969da)
![Web](https://img.shields.io/badge/Web-Flask-8250df)
![DB](https://img.shields.io/badge/DB-SQLite-003B57)
![Docker](https://img.shields.io/badge/Docker-CLI%20%2B%20Web-2496ED)
![Gestion](https://img.shields.io/badge/Gestion-Jira-0052CC)

Aplicacion desarrollada en Python para simular un taximetro digital. El sistema calcula el importe de un trayecto a partir del tiempo que el taxi permanece parado y del tiempo que esta en movimiento.

El proyecto se ha desarrollado como MVP academico dentro del bootcamp de Factoria F5, aplicando control de versiones con Git y GitHub, entorno virtual, ramas de trabajo, Pull Requests, tests unitarios, documentacion, tablero Kanban, SQLite, Docker, prototipado UX/UI en Figma, interfaz grafica de escritorio y version web con Flask.

## Indice

- [Estado del proyecto](#estado-del-proyecto)
- [Entregables](#entregables)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Funcionalidades](#funcionalidades)
- [Seguimiento del briefing](#seguimiento-del-briefing)
- [Instalacion local](#instalacion-local)
- [Ejecucion](#ejecucion)
- [Docker](#docker)
- [Base de datos](#base-de-datos)
- [Arquitectura y estructura](#arquitectura-y-estructura)
- [Testing y validacion](#testing-y-validacion)
- [Gestion del proyecto](#gestion-del-proyecto)
- [Mejoras futuras](#mejoras-futuras)

## Estado del proyecto

| Area | Estado | Resultado |
| --- | --- | --- |
| Nivel esencial | Completado | CLI funcional para gestionar trayectos. |
| Nivel medio | Completado | Logs, tests, historico y tarifas configurables. |
| Nivel avanzado | Completado | OOP, autenticacion y GUI de escritorio. |
| Nivel experto | Completado | SQLite, Docker y version web con Flask. |
| UX/UI | Completado | Prototipo web en Figma con flujo de usuario y criterios visuales. |
| Documentacion | En cierre | README y diario preparados para entrega. |

## Entregables

| Entregable | Estado | Enlace o ubicacion |
| --- | --- | --- |
| Repositorio GitHub con codigo fuente | Completado | https://github.com/Bootcamp-IA-MAD-P7/proyecto1_miguel-redondo |
| Tablero Kanban Jira | Completado | https://miguel-redondo.atlassian.net/jira/core/projects/TAXI/board?filter=&groupBy=status |
| Prototipo UX/UI Figma | Completado | https://www.figma.com/design/hfzWUpKkCrJsnI5ToBfTcq/Tax%C3%ADmetro-Digital-F5---Prototipo-Web?m=auto&t=TDCuPRO36jeoOvQw-6 |
| Demostracion CLI | Preparada | Ejecutable con `python taximetro.py` |
| Demostracion GUI | Preparada | Ejecutable con `python gui.py` |
| Demostracion Web | Preparada | Ejecutable con `python app.py` o Docker web |
| Presentacion para publico no tecnico | | Completado | https://canva.link/0mt9py82inlurfb |
| Presentacion tecnica del codigo | Pendiente de enlazar | [pendiente] |

## Tecnologias utilizadas

| Tecnologia / herramienta | Uso en el proyecto |
| --- | --- |
| Python 3.11 | Lenguaje principal. |
| Flask | Version web accesible desde navegador. |
| CustomTkinter | Interfaz grafica de escritorio. |
| SQLite | Persistencia estructurada de trayectos. |
| Pytest | Tests unitarios. |
| Logging | Trazabilidad tecnica. |
| JSON | Configuracion de tarifas y contrasena. |
| Docker | Contenedores para CLI y web. |
| Git | Control de versiones local. |
| GitHub | Repositorio remoto, ramas y Pull Requests. |
| Jira | Gestion del proyecto mediante tablero Kanban. |
| Figma | Prototipado UX/UI, flujo de usuario y apoyo visual. |
| Entorno virtual `.venv` | Aislamiento de dependencias. |

## Funcionalidades

- Calculo de tarifa por tiempo parado y tiempo en movimiento.
- CLI interactivo con comandos `start`, `stop`, `move`, `finish` y `exit`.
- Interfaz grafica de escritorio con CustomTkinter.
- Version web con Flask.
- Autenticacion basica por contrasena.
- Configuracion de tarifas desde `config.json`.
- Edicion de tarifas desde GUI y web antes de iniciar un trayecto.
- Bloqueo de tarifas durante un trayecto activo.
- Importe y tiempos actualizados durante el trayecto.
- Historico local en texto plano.
- Persistencia en SQLite.
- Visualizacion web de viajes registrados.
- Visualizacion web de logs tecnicos recientes.
- Dockerizacion del CLI.
- Dockerizacion de la web.
- Tests unitarios con `pytest`.
- Clase `Taximeter` para centralizar la logica del trayecto.

## Seguimiento del briefing

### Nivel esencial

![Nivel esencial](https://img.shields.io/badge/Nivel%20esencial-Completado-2ea44f)

| Check | Requisito | Estado |
| --- | --- | --- |
| OK | Programa CLI en Python. | ![Completado](https://img.shields.io/badge/Completado-2ea44f) |
| OK | Bienvenida y explicacion al iniciar. | ![Completado](https://img.shields.io/badge/Completado-2ea44f) |
| OK | Iniciar trayecto. | ![Completado](https://img.shields.io/badge/Completado-2ea44f) |
| OK | Calcular tarifa con taxi parado. | ![Completado](https://img.shields.io/badge/Completado-2ea44f) |
| OK | Calcular tarifa con taxi en movimiento. | ![Completado](https://img.shields.io/badge/Completado-2ea44f) |
| OK | Finalizar trayecto y mostrar total. | ![Completado](https://img.shields.io/badge/Completado-2ea44f) |
| OK | Iniciar nuevo trayecto sin cerrar el programa. | ![Completado](https://img.shields.io/badge/Completado-2ea44f) |

### Nivel medio

![Nivel medio](https://img.shields.io/badge/Nivel%20medio-Completado-d29922)

| Check | Requisito | Estado |
| --- | --- | --- |
| OK | Sistema de logs. | ![Completado](https://img.shields.io/badge/Completado-d29922) |
| OK | Tests unitarios. | ![Completado](https://img.shields.io/badge/Completado-d29922) |
| OK | Registro historico en texto plano. | ![Completado](https://img.shields.io/badge/Completado-d29922) |
| OK | Configuracion de precios. | ![Completado](https://img.shields.io/badge/Completado-d29922) |

### Nivel avanzado

![Nivel avanzado](https://img.shields.io/badge/Nivel%20avanzado-Completado-0969da)

| Check | Requisito | Estado |
| --- | --- | --- |
| OK | Refactorizacion con OOP. | ![Completado](https://img.shields.io/badge/Completado-0969da) |
| OK | Autenticacion con contrasena. | ![Completado](https://img.shields.io/badge/Completado-0969da) |
| OK | Interfaz grafica de usuario. | ![Completado](https://img.shields.io/badge/Completado-0969da) |

### Nivel experto

![Nivel experto](https://img.shields.io/badge/Nivel%20experto-Completado-8250df)

| Check | Requisito | Estado |
| --- | --- | --- |
| OK | Base de datos para trayectos. | ![SQLite](https://img.shields.io/badge/SQLite-Completado-2ea44f) |
| OK | Dockerizacion. | ![Docker](https://img.shields.io/badge/Docker-Completado-2496ED) |
| OK | Version web accesible desde navegador. | ![Flask](https://img.shields.io/badge/Flask-Completado-8250df) |

## Instalacion local

Clonar el repositorio:

```bash
git clone https://github.com/Bootcamp-IA-MAD-P7/proyecto1_miguel-redondo.git
cd proyecto1_miguel-redondo
```

Crear entorno virtual:

```bash
python -m venv .venv
```

Activar entorno virtual en Git Bash:

```bash
source .venv/Scripts/activate
```

Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

Comprobar instalacion:

```bash
python --version
python -m pytest
```

Resultado esperado:

```text
14 passed
```

## Configuracion

El archivo `config.json` centraliza tarifas y contrasena:

```json
{
  "stopped_rate": 0.02,
  "moving_rate": 0.05,
  "password": "admin123"
}
```

| Clave | Descripcion |
| --- | --- |
| `stopped_rate` | Tarifa por segundo cuando el taxi esta parado. |
| `moving_rate` | Tarifa por segundo cuando el taxi esta en movimiento. |
| `password` | Contrasena basica de acceso. |

Nota: la contrasena se guarda en texto plano porque se trata de un MVP academico. Como mejora futura se plantea un sistema de usuarios con credenciales protegidas.

## Ejecucion

### CLI

```bash
python taximetro.py
```

Comandos disponibles:

| Comando | Descripcion |
| --- | --- |
| `start` | Inicia un trayecto. |
| `stop` | Cambia el estado a parado. |
| `move` | Cambia el estado a movimiento. |
| `finish` | Finaliza el trayecto y muestra el total. |
| `exit` | Cierra el programa. |

### GUI de escritorio

```bash
python gui.py
```

Flujo principal:

1. Introducir contrasena.
2. Revisar o modificar tarifas.
3. Iniciar trayecto.
4. Cambiar entre parado y movimiento.
5. Finalizar trayecto.
6. Revisar importe final.

### Version web

```bash
python app.py
```

Acceso:

```text
http://localhost:5000
```

La web permite login, gestion del trayecto, contador en pantalla, cambio de tarifas antes de iniciar, consulta de viajes en SQLite y revision de logs tecnicos recientes.

## Docker

El proyecto incluye dos estrategias de contenedor:

| Archivo | Uso |
| --- | --- |
| `Dockerfile` | Ejecuta el CLI. |
| `Dockerfile.web` | Ejecuta la version web con Flask. |

### Docker CLI

Construir imagen:

```bash
docker build -t taximetro-cli .
```

Ejecutar CLI:

```bash
docker run --rm -it taximetro-cli
```

En Git Bash puede ser necesario usar:

```bash
winpty docker run --rm -it taximetro-cli
```

Ejecutar con persistencia:

```bash
docker run --rm -it -v taximetro_data:/app/data taximetro-cli
```

### Docker Web

Construir imagen:

```bash
docker build -f Dockerfile.web -t taximetro-web .
```

Ejecutar web:

```bash
docker run --rm -p 5000:5000 taximetro-web
```

Ejecutar web con persistencia:

```bash
docker run --rm -p 5000:5000 -v taximetro_web_data:/app/data taximetro-web
```

Acceso:

```text
http://localhost:5000
```

El uso de volumenes permite conservar `taximetro.db`, `taximetro.log` y `trip_history.txt` entre ejecuciones del contenedor.

## Base de datos

La aplicacion utiliza SQLite para almacenar trayectos finalizados. SQLite es suficiente para este MVP porque permite persistencia local sin servidor externo.

La tabla principal es `trips`.

| Campo | Tipo | Descripcion |
| --- | --- | --- |
| `id` | INTEGER | Identificador unico del trayecto. |
| `finished_at` | TEXT | Fecha y hora de finalizacion. |
| `stopped_time` | REAL | Tiempo total con el taxi parado. |
| `moving_time` | REAL | Tiempo total con el taxi en movimiento. |
| `stopped_rate` | REAL | Tarifa aplicada al tiempo parado. |
| `moving_rate` | REAL | Tarifa aplicada al tiempo en movimiento. |
| `total_fare` | REAL | Importe total del trayecto. |

### Criterio de normalizacion para el MVP

- Cada fila representa un trayecto finalizado.
- Cada campo almacena un dato atomico.
- `id` actua como clave primaria.
- Las tarifas se guardan dentro del viaje para conservar el precio historico aplicado.
- No se separan usuarios, tarifas o auditorias en tablas independientes porque no forman parte del alcance minimo actual.

Evolucion futura posible:

- Tabla `users`.
- Tabla `rates`.
- Tabla `audit_logs`.
- Relacion entre viajes y usuario autenticado.

### Como consultar SQLite

Desde Python:

```bash
python -c "import sqlite3; conn=sqlite3.connect('taximetro.db'); print(conn.execute('SELECT id, finished_at, total_fare FROM trips ORDER BY id DESC LIMIT 5').fetchall()); conn.close()"
```

Tambien puede revisarse con DB Browser for SQLite o extensiones de SQLite para VSCode.

## Arquitectura y estructura

```text
.
|-- .dockerignore
|-- .gitignore
|-- Dockerfile
|-- Dockerfile.web
|-- README.md
|-- app.py
|-- config.json
|-- database.py
|-- gui.py
|-- requirements.txt
|-- taximetro.py
|-- docs/
|   `-- diario-desarrollo.md
|-- static/
|   `-- css/
|       `-- styles.css
|-- templates/
|   |-- dashboard.html
|   `-- login.html
`-- tests/
    `-- test_taximetro.py
```

Responsabilidades principales:

| Archivo | Responsabilidad |
| --- | --- |
| `taximetro.py` | Logica principal, CLI, clase `Taximeter`, tarifas, autenticacion e historico. |
| `database.py` | Creacion y consulta de SQLite. |
| `gui.py` | Interfaz grafica de escritorio. |
| `app.py` | Aplicacion web Flask. |
| `templates/` | Vistas HTML de la web. |
| `static/css/styles.css` | Estilos de la web. |
| `tests/test_taximetro.py` | Tests unitarios. |

Archivos generados localmente y no versionados:

| Archivo | Uso |
| --- | --- |
| `taximetro.log` | Logs tecnicos. |
| `trip_history.txt` | Historico en texto plano. |
| `taximetro.db` | Base de datos SQLite. |
| `.venv/` | Entorno virtual. |
| `.pytest_cache/` | Cache de pytest. |
| `__pycache__/` | Cache de Python. |

## Testing y validacion

Comandos de validacion habituales:

```bash
python -m py_compile taximetro.py
python -m py_compile database.py
python -m py_compile gui.py
python -m py_compile app.py
python -m pytest
git diff --check
```

Resultado actual:

```text
14 tests pasados
```

Se validan calculos de tarifa, configuracion, autenticacion, estados de la clase `Taximeter`, finalizacion de trayectos, persistencia SQLite y lectura de registros.

## Gestion del proyecto

El trabajo se ha gestionado con Jira y GitHub.

Flujo aplicado:

1. `main` como rama estable.
2. Rama por funcionalidad o bloque de documentacion.
3. Commits descriptivos con Conventional Commits.
4. Pull Request hacia `main`.
5. Validacion antes de fusionar.
6. Actualizacion local de `main` tras cada merge.

Ramas principales utilizadas:

- `feature/nivel-esencial`
- `feature/logs`
- `feature/tests-unitarios`
- `feature/historico-trayectos`
- `feature/configuracion-tarifas`
- `feature/oop-taximeter`
- `feature/autenticacion-basica`
- `feature/gui-customtkinter`
- `feature/sqlite-database`
- `feature/docker-CLI`
- `feature/flask-web`
- `feature/docker-web`
- `docs/estilo-profesional`
- `docs/readme-guia-uso`

## Diario de desarrollo

El proceso de trabajo, decisiones tecnicas, problemas encontrados y validaciones realizadas se documentan en el diario de desarrollo:

[Ver diario de desarrollo](docs/diario-desarrollo.md)

## UX/UI

La version web se prototipo en Figma antes de implementarse. El objetivo visual fue crear una interfaz oscura, sobria y moderna, con una inspiracion ligera en taximetros clasicos.

El prototipo incluye:

- Dashboard principal.
- Pantallas web.
- Componentes base.
- Flujo de usuario.
- Diagramas de apoyo.
- Persona y casos de uso.

Enlace al prototipo:

```text
https://www.figma.com/design/hfzWUpKkCrJsnI5ToBfTcq/Tax%C3%ADmetro-Digital-F5---Prototipo-Web?m=auto&t=TDCuPRO36jeoOvQw-6
```

## Enfoque MVP

El proyecto se ha planteado como una evolucion incremental:

```text
CLI minimo -> logs y tests -> OOP -> GUI -> SQLite -> Docker -> Web Flask
```

La idea inicial era resolver primero el problema esencial: calcular una tarifa. A partir de ahi se han anadido capas de calidad, persistencia, usabilidad y despliegue.

## Mejoras futuras

- Gestion real de usuarios.
- Hash de contrasenas.
- Separacion de tarifas en tabla propia.
- API REST para consultar trayectos.
- Tests especificos para Flask.
- Despliegue en plataforma cloud.
- Panel administrativo para consultar historico y logs con filtros.

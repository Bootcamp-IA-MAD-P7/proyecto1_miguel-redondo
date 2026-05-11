# Proyecto 1 - Taximetro Digital

![Python](https://img.shields.io/badge/Python-3.11-3776AB)
![Estado](https://img.shields.io/badge/Estado-Nivel%20avanzado%20completado-2ea44f)
![Tests](https://img.shields.io/badge/Tests-12%20passed-2ea44f)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-0969da)
![Gestion](https://img.shields.io/badge/Gestion-Jira-0052CC)

Aplicacion desarrollada en Python para simular un taximetro digital. El sistema calcula el importe de un trayecto a partir del tiempo que el taxi permanece parado y del tiempo que esta en movimiento.

El proyecto forma parte del bootcamp de Factoria F5 y se ha desarrollado de forma incremental, utilizando entorno virtual, Git, ramas de trabajo, Pull Requests, tests unitarios, documentacion tecnica y gestion de tareas con Jira.

## Estado Del Proyecto

El proyecto cubre actualmente los niveles esencial, medio y avanzado del briefing.

| Nivel | Estado | Resultado |
| --- | --- | --- |
| Esencial | ✅ Completado | CLI funcional para gestionar trayectos. |
| Medio | ✅ Completado | Logs, tests, historico y tarifas configurables. |
| Avanzado | ✅ Completado | OOP, autenticacion y GUI de escritorio. |
| Experto | ⬜ Pendiente | Base de datos, Docker y version web. |

## Seguimiento Del Briefing

### ![Nivel Esencial](https://img.shields.io/badge/Nivel%20Esencial-Completado-2ea44f)

| Check | Requisito | Estado |
| --- | --- | --- |
| ✅ | Desarrollar un programa CLI en Python. | Completado |
| ✅ | Mostrar bienvenida y explicar el funcionamiento al iniciar. | Completado |
| ✅ | Iniciar un trayecto. | Completado |
| ✅ | Calcular tarifa con el taxi parado. | Completado |
| ✅ | Calcular tarifa con el taxi en movimiento. | Completado |
| ✅ | Finalizar un trayecto y mostrar el total en euros. | Completado |
| ✅ | Permitir iniciar un nuevo trayecto sin cerrar el programa. | Completado |

### ![Nivel Medio](https://img.shields.io/badge/Nivel%20Medio-Completado-d29922)

| Check | Requisito | Estado |
| --- | --- | --- |
| ✅ | Implementar logs para trazabilidad. | Completado |
| ✅ | Agregar tests unitarios. | Completado |
| ✅ | Crear un registro historico de trayectos en texto plano. | Completado |
| ✅ | Permitir la configuracion de precios para adaptarse a la demanda. | Completado |

### ![Nivel Avanzado](https://img.shields.io/badge/Nivel%20Avanzado-Completado-0969da)

| Check | Requisito | Estado |
| --- | --- | --- |
| ✅ | Refactorizar el codigo con programacion orientada a objetos. | Completado |
| ✅ | Implementar autenticacion con contrasena. | Completado |
| ✅ | Desarrollar una interfaz grafica de usuario. | Completado |

### ![Nivel Experto](https://img.shields.io/badge/Nivel%20Experto-Pendiente-8250df)

| Check | Requisito | Estado |
| --- | --- | --- |
| ⬜ | Integrar una base de datos para almacenar trayectos. | Pendiente |
| ⬜ | Dockerizar la aplicacion. | Pendiente |
| ⬜ | Desarrollar una version web accesible desde navegador. | Pendiente |

## Funcionalidades Principales

- Calculo de tarifa por tiempo parado y tiempo en movimiento.
- CLI interactivo con comandos `start`, `stop`, `move`, `finish` y `exit`.
- Interfaz grafica de escritorio con CustomTkinter.
- Autenticacion basica por contrasena.
- Configuracion de tarifas desde `config.json`.
- Edicion de tarifas desde la GUI antes de iniciar un trayecto.
- Bloqueo de cambio de tarifas durante un trayecto activo.
- Logs tecnicos con `logging`.
- Historico local de trayectos finalizados.
- Tests unitarios con `pytest`.
- Clase `Taximeter` para centralizar el estado y la logica del trayecto.

## Tecnologias Y Herramientas

| Tecnologia | Uso |
| --- | --- |
| Python 3.11 | Lenguaje principal del proyecto. |
| CustomTkinter | Interfaz grafica de escritorio. |
| Pytest | Tests unitarios. |
| Logging | Trazabilidad tecnica. |
| JSON | Configuracion de tarifas y contrasena. |
| Git | Control de versiones. |
| GitHub | Repositorio remoto, ramas y Pull Requests. |
| Jira | Gestion del proyecto mediante tablero Kanban. |
| Entorno virtual `.venv` | Aislamiento de dependencias. |

## Estructura Del Proyecto

```text
.
|-- .gitignore
|-- config.json
|-- gui.py
|-- README.md
|-- requirements.txt
|-- taximetro.py
|-- docs/
|   `-- diario-desarrollo.md
`-- tests/
    `-- test_taximetro.py
```

Archivos generados localmente y no versionados:

| Archivo | Uso |
| --- | --- |
| `taximetro.log` | Logs tecnicos de la aplicacion. |
| `trip_history.txt` | Historico de trayectos finalizados. |
| `.venv/` | Entorno virtual local. |
| `.pytest_cache/` | Cache local de pytest. |
| `__pycache__/` | Cache local de Python. |

## Instalacion Desde Cero

Clonar el repositorio:

```bash
git clone https://github.com/Bootcamp-IA-MAD-P7/proyecto1_miguel-redondo.git
cd proyecto1_miguel-redondo
```

Crear el entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Git Bash:

```bash
source .venv/Scripts/activate
```

Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

Comprobar la instalacion:

```bash
python --version
python -m pytest
```

Resultado esperado:

```text
12 passed
```

## Configuracion

El archivo `config.json` centraliza valores configurables:

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

Tarifas por defecto:

- Taxi parado: `0.02` euros/segundo.
- Taxi en movimiento: `0.05` euros/segundo.

La GUI permite modificar las tarifas antes de iniciar un trayecto. Si no se modifican, se usan las tarifas definidas en `config.json`.

Nota tecnica: la contrasena se guarda en texto plano porque se trata de una autenticacion basica para un MVP academico. Como mejora futura se plantea crear un sistema de gestion de usuarios.

## Ejecucion

El proyecto puede ejecutarse de dos formas.

### Interfaz Grafica

```bash
python gui.py
```

Flujo de uso:

1. Introducir la contrasena.
2. Revisar las tarifas cargadas.
3. Modificar tarifas si es necesario.
4. Pulsar `Aplicar tarifas`.
5. Pulsar `Iniciar`.
6. Cambiar entre `Parado` y `Movimiento`.
7. Pulsar `Finalizar`.
8. Revisar el importe final y el resumen del ultimo trayecto.

Comportamiento de la GUI:

- Al iniciar un trayecto, el taxi empieza en estado parado.
- La luz de estado aparece en gris cuando no hay trayecto activo.
- La luz cambia a ambar cuando el taxi esta parado.
- La luz parpadea en verde cuando el taxi esta en movimiento.
- La luz queda en verde fijo al finalizar.
- El importe se actualiza en tiempo real.
- El total final se muestra destacado.
- El trayecto finalizado se guarda en `trip_history.txt`.
- Las acciones principales se registran en `taximetro.log`.

### Linea De Comandos

```bash
python taximetro.py
```

Comandos disponibles:

| Comando | Descripcion | Requiere trayecto activo |
| --- | --- | --- |
| `start` | Inicia un trayecto. | No |
| `stop` | Cambia el estado del taxi a parado. | Si |
| `move` | Cambia el estado del taxi a movimiento. | Si |
| `finish` | Finaliza el trayecto y muestra el importe total. | Si |
| `exit` | Cierra el programa. | No |

Ejemplo de uso:

```text
Introduce la contrasena: admin123
Acceso concedido.

Bienvenido al Taximetro Digital F5
Tarifas: parado = 0.02 euros/segundo | movimiento = 0.05 euros/segundo

> start
Trayecto iniciado. Estado inicial: parado.
> move
Estado actualizado: en movimiento.
> stop
Estado actualizado: parado.
> finish

--- Resumen del trayecto ---
Tiempo parado: 5.4 segundos
Tiempo en movimiento: 8.2 segundos
Importe total: 0.52 euros
----------------------------

> exit
Saliendo del programa. Hasta pronto.
```

## Calculo De Tarifa

La tarifa se calcula mediante la funcion `calculate_fare`:

```text
importe = segundos_parado * tarifa_parado + segundos_movimiento * tarifa_movimiento
```

Ejemplo:

```text
10 segundos parado * 0.02 = 0.20 euros
5 segundos en movimiento * 0.05 = 0.25 euros
total = 0.45 euros
```

El tiempo se mide en tiempo real, por lo que pueden aparecer decimales en los segundos registrados. El importe se muestra redondeado a dos decimales.

## Tests

Ejecutar la suite de tests:

```bash
python -m pytest
```

Actualmente se validan:

- Calculo de tarifa con tarifas por defecto.
- Calculo de tarifa con tarifas configurables.
- Carga de contrasena desde configuracion.
- Estado inicial de la clase `Taximeter`.
- Inicio de trayecto.
- Prevencion de trayectos duplicados.
- Rechazo de estados invalidos.
- Finalizacion sin trayecto activo.
- Resumen devuelto al finalizar un trayecto.

Resultado actual:

```text
12 tests pasados
```

## Flujo De Trabajo Con Git

El proyecto se ha desarrollado siguiendo un flujo basado en ramas:

1. Mantener `main` como rama estable.
2. Crear una rama para cada funcionalidad.
3. Trabajar en cambios pequenos y verificables.
4. Ejecutar validaciones antes de confirmar cambios.
5. Crear commits descriptivos siguiendo Conventional Commits.
6. Subir la rama a GitHub.
7. Abrir Pull Request.
8. Fusionar en `main`.
9. Actualizar `main` local con `git pull`.

Ramas utilizadas:

- `feature/nivel-esencial`
- `feature/logs`
- `feature/tests-unitarios`
- `feature/historico-trayectos`
- `feature/configuracion-tarifas`
- `feature/oop-taximeter`
- `feature/autenticacion-basica`
- `feature/gui-customtkinter`
- `docs/estilo-profesional`
- `docs/readme-guia-uso`

Comprobaciones habituales:

```bash
git status
python -m py_compile taximetro.py
python -m py_compile gui.py
python -m pytest
git diff --check
```

## Gestion Del Proyecto

El seguimiento del trabajo se realiza mediante un tablero Kanban en Jira:

[Ver tablero Jira](https://miguel-redondo.atlassian.net/jira/core/projects/TAXI/board?filter=&groupBy=status)

Estado actual:

- Nivel esencial completado.
- Nivel medio completado.
- Nivel avanzado completado.
- Nivel experto pendiente.

## Documentacion Del Proceso

El registro de decisiones, avances, problemas y validaciones se mantiene en:

[docs/diario-desarrollo.md](docs/diario-desarrollo.md)

## Roadmap

Proximos pasos previstos:

- Integrar una base de datos SQLite para almacenar trayectos.
- Dockerizar la aplicacion.
- Desarrollar una version web accesible desde navegador.
- Valorar un sistema de gestion de usuarios para sustituir la contrasena unica del MVP.

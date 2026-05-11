# Proyecto 1 - Taximetro Digital

Aplicacion desarrollada en Python para simular un taximetro digital. El sistema calcula el importe de un trayecto a partir del tiempo que el taxi permanece parado y del tiempo que esta en movimiento.

El proyecto forma parte del bootcamp de Factoria F5 y se esta desarrollando de forma incremental, aplicando control de versiones, ramas de trabajo, Pull Requests, documentacion tecnica, tests y gestion de tareas con Jira.

## Estado Actual

El proyecto tiene completados el nivel esencial y el nivel medio del briefing. Tambien se ha iniciado el nivel avanzado con una refactorizacion a programacion orientada a objetos.

Estado funcional actual:

- CLI operativo.
- Calculo de tarifas por tiempo parado y tiempo en movimiento.
- Logs tecnicos.
- Tests unitarios.
- Historico de trayectos en archivo de texto.
- Configuracion externa de tarifas.
- Clase `Taximeter` para gestionar el estado del trayecto.

## Funcionalidades

### Nivel Esencial

- Interfaz de linea de comandos.
- Mensaje inicial de bienvenida y explicacion de uso.
- Inicio de trayecto.
- Cambio de estado entre parado y movimiento.
- Finalizacion de trayecto.
- Calculo del importe total.
- Posibilidad de iniciar nuevos trayectos sin cerrar el programa.

### Nivel Medio

- Sistema de logs con `logging`.
- Tests unitarios con `pytest`.
- Registro historico de trayectos en archivo de texto plano.
- Configuracion de tarifas mediante `config.json`.

### Nivel Avanzado En Curso

- Refactorizacion inicial con programacion orientada a objetos.
- Clase `Taximeter` para centralizar el estado del trayecto.
- Metodos principales:
  - `start_trip`
  - `change_state`
  - `finish_trip`

## Estructura Principal

```text
.
|-- config.json
|-- README.md
|-- requirements.txt
|-- taximetro.py
|-- docs/
|   `-- diario-desarrollo.md
`-- tests/
    `-- test_taximetro.py
```

## Tarifas

Las tarifas se definen en `config.json`:

```json
{
  "stopped_rate": 0.02,
  "moving_rate": 0.05
}
```

Tarifas actuales:

- Taxi parado: 0.02 euros/segundo.
- Taxi en movimiento: 0.05 euros/segundo.

## Requisitos

- Python 3.11
- Git
- Entorno virtual dentro del proyecto

## Instalacion

Clonar el repositorio:

```bash
git clone https://github.com/Bootcamp-IA-MAD-P7/proyecto1_miguel-redondo.git
cd proyecto1_miguel-redondo
```

Crear y activar el entorno virtual:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

## Ejecucion

Ejecutar la aplicacion CLI:

```bash
python taximetro.py
```

Comandos disponibles:

| Comando | Descripcion |
| --- | --- |
| `start` | Inicia un trayecto. |
| `stop` | Indica que el taxi esta parado. |
| `move` | Indica que el taxi esta en movimiento. |
| `finish` | Finaliza el trayecto y muestra el importe total. |
| `exit` | Cierra el programa. |

## Tests

Ejecutar la suite de tests:

```bash
python -m pytest
```

Actualmente se validan:

- Calculo de tarifa con tarifas por defecto.
- Calculo de tarifa con tarifas configurables.
- Estado inicial de la clase `Taximeter`.
- Inicio de trayecto.
- Prevencion de trayectos duplicados.
- Finalizacion sin trayecto activo.
- Resumen devuelto al finalizar un trayecto.

Resultado actual:

```text
10 tests pasados
```

## Archivos Generados Localmente

Durante la ejecucion se pueden generar archivos locales que no se versionan en Git:

| Archivo | Uso |
| --- | --- |
| `taximetro.log` | Trazabilidad tecnica de la aplicacion. |
| `trip_history.txt` | Historico funcional de trayectos finalizados. |

Ambos archivos estan ignorados en `.gitignore`.

## Flujo De Trabajo

El proyecto se desarrolla con un flujo basado en ramas:

1. Partir de `main` limpio y actualizado.
2. Crear una rama para cada funcionalidad.
3. Implementar cambios pequenos y verificables.
4. Ejecutar pruebas.
5. Crear commits descriptivos.
6. Subir la rama a GitHub.
7. Abrir Pull Request.
8. Fusionar en `main`.
9. Actualizar `main` local.

Ejemplos de ramas utilizadas:

- `feature/nivel-esencial`
- `feature/logs`
- `feature/tests-unitarios`
- `feature/historico-trayectos`
- `feature/configuracion-tarifas`
- `feature/oop-taximeter`

## Gestion Del Proyecto

El seguimiento del trabajo se realiza mediante un tablero Kanban en Jira:

[Ver tablero Jira](https://miguel-redondo.atlassian.net/jira/core/projects/TAXI/board?filter=&groupBy=status)

Estado actual:

- 8 tareas finalizadas.
- Nivel esencial completado.
- Nivel medio completado.
- Nivel avanzado iniciado.

## Documentacion Del Proceso

El registro de decisiones, avances, problemas y validaciones se mantiene en:

[docs/diario-desarrollo.md](docs/diario-desarrollo.md)

## Proximos Pasos

- Implementar autenticacion basica.
- Preparar una interfaz grafica.
- Evolucionar el historico hacia base de datos SQLite.
- Preparar Docker y version web para el nivel experto.

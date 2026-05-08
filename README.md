# Proyecto 1 - Taximetro Digital

Proyecto desarrollado en Python para simular un taximetro digital que calcula tarifas segun el tiempo que el taxi permanece parado y el tiempo que esta en movimiento.

## Estado del proyecto

El proyecto se encuentra en desarrollo. Actualmente estan completados el nivel esencial y el nivel medio del briefing.

El programa ya permite trabajar desde una interfaz CLI, registrar eventos mediante logs, ejecutar tests unitarios, guardar un historico de trayectos y configurar tarifas desde un archivo externo.

## Funcionalidades implementadas

### Nivel esencial

- Aplicacion CLI en Python.
- Bienvenida y explicacion inicial del funcionamiento.
- Inicio de trayecto con `start`.
- Cambio a estado parado con `stop`.
- Cambio a estado en movimiento con `move`.
- Finalizacion de trayecto con `finish`.
- Calculo del importe total en euros.
- Posibilidad de iniciar un nuevo trayecto sin cerrar el programa.

### Nivel medio

- Sistema de logs con `logging`.
- Tests unitarios con `pytest`.
- Historico de trayectos en archivo de texto plano.
- Configuracion de tarifas mediante `config.json`.

## Tarifas actuales

Las tarifas se configuran en el archivo `config.json`:

```json
{
  "stopped_rate": 0.02,
  "moving_rate": 0.05
}
```

- Taxi parado: 0.02 euros/segundo
- Taxi en movimiento: 0.05 euros/segundo

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

```bash
python taximetro.py
```

## Comandos del CLI

- `start`: iniciar un trayecto.
- `stop`: indicar que el taxi esta parado.
- `move`: indicar que el taxi esta en movimiento.
- `finish`: finalizar el trayecto y mostrar el importe total.
- `exit`: salir del programa.

## Tests

Ejecutar la suite de tests:

```bash
python -m pytest
```

Actualmente se validan los calculos de tarifa con tarifas por defecto y tarifas configurables.

## Archivos generados localmente

Durante la ejecucion se pueden crear archivos locales que no se suben a GitHub:

- `taximetro.log`: trazabilidad tecnica del programa.
- `trip_history.txt`: historico de trayectos finalizados.

Estos archivos estan ignorados en `.gitignore`.

## Gestion del proyecto

El proyecto se organiza mediante un tablero Kanban en Jira:

[Ver tablero Jira](https://miguel-redondo.atlassian.net/jira/core/projects/TAXI/board?filter=&groupBy=status)

Estado actual del tablero: 7 tareas finalizadas.

## Diario de desarrollo

El registro diario de decisiones, avances y problemas se encuentra en:

[docs/diario-desarrollo.md](docs/diario-desarrollo.md)

## Proximos pasos

- Empezar el nivel avanzado.
- Refactorizar el codigo con programacion orientada a objetos.
- Implementar autenticacion basica.
- Preparar una interfaz grafica.
- Evolucionar el historico hacia base de datos SQLite.
- Preparar Docker y version web para el nivel experto.

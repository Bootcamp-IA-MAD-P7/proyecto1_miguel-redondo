# Proyecto 1 - Taximetro Digital

Proyecto desarrollado en Python para simular un taximetro digital que calcula tarifas segun el tiempo que el taxi permanece parado y el tiempo que esta en movimiento.

## Estado del proyecto

El proyecto se encuentra en desarrollo. Actualmente se esta trabajando en el nivel esencial: una aplicacion CLI funcional para iniciar trayectos, cambiar el estado del taxi, finalizar viajes y calcular el importe total.

## Tarifas actuales

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

## Gestion del proyecto

El proyecto se organiza mediante un tablero Kanban en Jira:

[Ver tablero Jira](https://miguel-redondo.atlassian.net/jira/core/projects/TAXI/board?filter=&groupBy=status)

## Diario de desarrollo

El registro diario de decisiones, avances y problemas se encuentra en:

[docs/diario-desarrollo.md](docs/diario-desarrollo.md)

## Proximos pasos

- Completar el nivel esencial del CLI.
- Documentar el uso del proyecto.
- Implementar logs.
- Agregar tests unitarios.
- Guardar historico de trayectos.
- Refactorizar el codigo con OOP.
- Preparar base de datos, Docker y version web para el nivel experto.

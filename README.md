# Proyecto 1 - Taximetro Digital

Aplicacion desarrollada en Python para simular un taximetro digital. El sistema calcula el importe de un trayecto a partir del tiempo que el taxi permanece parado y del tiempo que esta en movimiento.

El proyecto forma parte del bootcamp de Factoria F5 y se esta desarrollando de forma incremental, aplicando control de versiones, ramas de trabajo, Pull Requests, documentacion tecnica, tests y gestion de tareas con Jira.

## Estado Actual

El proyecto tiene completados el nivel esencial y el nivel medio del briefing. Tambien se ha iniciado el nivel avanzado, incorporando programacion orientada a objetos y autenticacion basica por contrasena.

Estado funcional actual:

- CLI operativo.
- Autenticacion basica antes de acceder al programa.
- Calculo de tarifas por tiempo parado y tiempo en movimiento.
- Logs tecnicos.
- Tests unitarios.
- Historico de trayectos en archivo de texto.
- Configuracion externa de tarifas y contrasena.
- Clase `Taximeter` para gestionar el estado del trayecto.

## Seguimiento Del Briefing

Esta tabla resume los requisitos del briefing y el estado de avance del proyecto.

### ![Nivel Esencial](https://img.shields.io/badge/Nivel%20Esencial-Completado-2ea44f)

| Check | Requisito | Estado |
| --- | --- | --- |
| ✅ | Desarrollar un programa CLI en Python. | Completado |
| ✅ | Mostrar bienvenida y explicacion de funcionamiento al iniciar. | Completado |
| ✅ | Iniciar un trayecto. | Completado |
| ✅ | Calcular tarifa con el taxi parado. | Completado |
| ✅ | Calcular tarifa con el taxi en movimiento. | Completado |
| ✅ | Finalizar un trayecto y mostrar el total en euros. | Completado |
| ✅ | Permitir iniciar un nuevo trayecto sin cerrar el programa. | Completado |

### ![Nivel Medio](https://img.shields.io/badge/Nivel%20Medio-Completado-d29922)

| Check | Requisito | Estado |
| --- | --- | --- |
| ✅ | Implementar un sistema de logs para trazabilidad. | Completado |
| ✅ | Agregar tests unitarios. | Completado |
| ✅ | Crear un registro historico de trayectos en texto plano. | Completado |
| ✅ | Permitir la configuracion de precios. | Completado |

### ![Nivel Avanzado](https://img.shields.io/badge/Nivel%20Avanzado-En%20curso-0969da)

| Check | Requisito | Estado |
| --- | --- | --- |
| ✅ | Refactorizar el codigo con programacion orientada a objetos. | Completado |
| ✅ | Implementar autenticacion con contrasena. | Completado |
| ⏳ | Desarrollar una interfaz grafica de usuario. | En desarrollo |

### ![Nivel Experto](https://img.shields.io/badge/Nivel%20Experto-Pendiente-8250df)

| Check | Requisito | Estado |
| --- | --- | --- |
| ⬜ | Integrar una base de datos para almacenar trayectos. | Pendiente |
| ⬜ | Dockerizar la aplicacion. | Pendiente |
| ⬜ | Desarrollar una version web accesible desde navegador. | Pendiente |

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
- Autenticacion basica con contrasena configurada en `config.json`.

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

## Requisitos

| Requisito | Uso |
| --- | --- |
| Python 3.11 | Ejecutar la aplicacion y los tests. |
| Git | Control de versiones y trabajo con ramas. |
| GitHub | Repositorio remoto y Pull Requests. |
| Entorno virtual `.venv` | Aislar dependencias del proyecto. |

## Dependencias

Las dependencias del proyecto estan declaradas en `requirements.txt`.

Dependencia principal:

| Paquete | Uso |
| --- | --- |
| `pytest` | Ejecucion de tests unitarios. |

Instalacion de dependencias:

```bash
python -m pip install -r requirements.txt
```

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

Comprobar que el entorno esta activo:

```bash
python --version
python -m pytest
```

Resultado esperado de tests:

```text
11 tests pasados
```

## Configuracion

El archivo `config.json` centraliza valores configurables de la aplicacion:

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
| `password` | Contrasena basica para acceder al programa. |

Tarifas actuales:

- Taxi parado: 0.02 euros/segundo.
- Taxi en movimiento: 0.05 euros/segundo.

Nota tecnica: la contrasena esta en texto plano porque se trata de una autenticacion basica de nivel academico. Una mejora futura seria almacenarla con hash.

## Ejecucion Del Programa

Ejecutar la aplicacion CLI:

```bash
python taximetro.py
```

Al arrancar, el programa solicita una contrasena:

```text
Introduce la contrasena:
```

Contrasena configurada por defecto:

```text
admin123
```

Si la contrasena es correcta, el programa muestra el menu principal. Si se introducen tres contrasenas incorrectas, el acceso se deniega y el programa finaliza.

## Funcionamiento Del CLI

Flujo habitual de uso:

1. Ejecutar `python taximetro.py`.
2. Introducir la contrasena.
3. Iniciar un trayecto con `start`.
4. Cambiar a movimiento con `move`.
5. Cambiar a parado con `stop` cuando corresponda.
6. Finalizar el trayecto con `finish`.
7. Revisar el resumen mostrado.
8. Iniciar otro trayecto o salir con `exit`.

Comandos disponibles:

| Comando | Descripcion | Requiere trayecto activo |
| --- | --- | --- |
| `start` | Inicia un trayecto. | No |
| `stop` | Cambia el estado del taxi a parado. | Si |
| `move` | Cambia el estado del taxi a movimiento. | Si |
| `finish` | Finaliza el trayecto y muestra el importe total. | Si |
| `exit` | Cierra el programa. | No |

Ejemplo de ejecucion:

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

La tarifa se calcula con la funcion `calculate_fare`:

```text
importe = segundos_parado * tarifa_parado + segundos_movimiento * tarifa_movimiento
```

Ejemplo:

```text
10 segundos parado * 0.02 = 0.20 euros
5 segundos en movimiento * 0.05 = 0.25 euros
total = 0.45 euros
```

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
- Finalizacion sin trayecto activo.
- Resumen devuelto al finalizar un trayecto.

Resultado actual:

```text
11 tests pasados
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
- `feature/autenticacion-basica`

## Gestion Del Proyecto

El seguimiento del trabajo se realiza mediante un tablero Kanban en Jira:

[Ver tablero Jira](https://miguel-redondo.atlassian.net/jira/core/projects/TAXI/board?filter=&groupBy=status)

Estado actual:

- Nivel esencial completado.
- Nivel medio completado.
- Nivel avanzado iniciado.

## Documentacion Del Proceso

El registro de decisiones, avances, problemas y validaciones se mantiene en:

[docs/diario-desarrollo.md](docs/diario-desarrollo.md)

## Proximos Pasos

- Preparar una interfaz grafica.
- Evolucionar el historico hacia base de datos SQLite.
- Preparar Docker y version web para el nivel experto.

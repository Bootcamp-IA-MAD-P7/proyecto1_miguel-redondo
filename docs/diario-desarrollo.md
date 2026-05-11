# Diario De Desarrollo

Este documento registra el avance diario del proyecto. Su objetivo es conservar decisiones, problemas, validaciones y cambios relevantes para facilitar el aprendizaje, la trazabilidad y la defensa tecnica del trabajo.

## Dia 1 - 7 de mayo de 2026

### Objetivos

- Crear el repositorio oficial en la organizacion del bootcamp.
- Preparar el proyecto en local.
- Configurar un entorno virtual aislado.
- Subir el codigo base.
- Crear una rama de trabajo para el nivel esencial.
- Probar el flujo inicial del CLI.
- Crear el tablero Kanban en Jira.
- Empezar a mejorar la experiencia de uso del programa.

### Trabajo Realizado

- Se creo el repositorio `proyecto1_miguel-redondo` en `Bootcamp-IA-MAD-P7`.
- Se preparo la carpeta local dentro de `Bootcamp-FactoriaF5`.
- Se creo y activo el entorno virtual `.venv`.
- Se configuro `.gitignore` para excluir `.venv/` y `__pycache__/`.
- Se anadio el codigo base en `taximetro.py`.
- Se creo un `README.md` inicial.
- Se subio la rama `main` al repositorio remoto.
- Se creo la rama `feature/nivel-esencial`.
- Se probo el flujo basico: iniciar, mover, parar, finalizar y salir.
- Se elimino un mensaje de depuracion del calculo de tarifa.
- Se extrajeron las tarifas a constantes:
  - `STOPPED_RATE`
  - `MOVING_RATE`
- Se mejoraron los mensajes del CLI.
- Se creo el tablero Jira para gestionar el proyecto.

### Decisiones

- Usar Git Bash para comandos del proyecto.
- Usar VSCode como editor principal.
- Mantener el entorno virtual dentro del proyecto.
- No trabajar directamente sobre `main`.
- Usar ramas `feature/...` para funcionalidades.
- Usar commits pequenos y descriptivos siguiendo Conventional Commits.
- Usar Jira como soporte de gestion del proyecto.

### Problemas Y Aprendizajes

- Al importar el modulo aparecio `__pycache__/`.
- Se soluciono anadiendo `__pycache__/` al `.gitignore`.
- Durante una prueba, `calculate_fare` llego a devolver `None` por un cambio incompleto.
- Se corrigio la funcion y se valido con:

```bash
python -c "from taximetro import calculate_fare; print(calculate_fare(10, 5))"
```

### Estado Al Cierre

- Repositorio creado y subido a GitHub.
- Entorno virtual configurado.
- Rama `feature/nivel-esencial` creada y subida.
- CLI funcional y probado.
- Jira iniciado.
- Documentacion inicial creada.

### Siguiente Paso

- Completar el nivel esencial y avanzar hacia el nivel medio.

## Dia 2 - 8 de mayo de 2026

### Objetivos

- Continuar desde `main` limpio y sincronizado.
- Completar las tareas del nivel medio.
- Mantener un flujo profesional con ramas, commits, Pull Requests y Jira.
- Entender cada cambio antes de implementarlo.

### Trabajo Realizado

#### Sistema De Logs

- Se creo la rama `feature/logs`.
- Se configuro `logging`.
- Se registraron eventos principales con `INFO`.
- Se registraron usos incorrectos con `WARNING`.
- Se anadio `*.log` al `.gitignore`.
- Se fusiono la funcionalidad mediante Pull Request.

#### Tests Unitarios

- Se creo la rama `feature/tests-unitarios`.
- Se instalo `pytest` dentro del entorno virtual.
- Se genero `requirements.txt`.
- Se creo la carpeta `tests/`.
- Se creo `tests/test_taximetro.py`.
- Se validaron varios casos de calculo de tarifa.
- Se fusiono la funcionalidad mediante Pull Request.

#### Historico De Trayectos

- Se creo la rama `feature/historico-trayectos`.
- Se creo la funcion `save_trip_history`.
- Se guardan trayectos finalizados en `trip_history.txt`.
- Se anadio `trip_history.txt` al `.gitignore`.
- Se fusiono la funcionalidad mediante Pull Request.

#### Configuracion De Tarifas

- Se creo la rama `feature/configuracion-tarifas`.
- Se creo `config.json`.
- Se creo la funcion `load_rates`.
- `calculate_fare` paso a aceptar tarifas configurables.
- Se anadio un test para tarifas personalizadas.
- Se fusiono la funcionalidad mediante Pull Request.

### Validaciones

```bash
python -m py_compile taximetro.py
python taximetro.py
python -m pytest
```

Tambien se revisaron manualmente:

- `taximetro.log`
- `trip_history.txt`
- comportamiento del programa al modificar temporalmente `config.json`

### Decisiones

- Mantener `main` como rama estable.
- Crear una rama por cada tarea importante.
- Fusionar mediante Pull Request despues de validar.
- No versionar logs ni historicos generados localmente.
- Usar `config.json` para modificar tarifas sin tocar codigo.
- Usar `pytest` como herramienta de testing.
- Documentar al final del dia para no interrumpir el ritmo de desarrollo.

### Problemas Y Aprendizajes

- Un error al escribir `py_compile` impidio ejecutar la comprobacion de sintaxis.
- Se corrigio usando:

```bash
python -m py_compile taximetro.py
```

- `load_rates` llego a devolver `None` porque faltaba retornar las tarifas.
- Se corrigio con `return stopped_rate, moving_rate`.
- Un `print` de tarifas necesitaba ser f-string para mostrar los valores reales.
- Se reforzo el habito de probar antes de hacer commit.

### Estado Al Cierre

- Nivel esencial completado.
- Nivel medio completado.
- 7 tareas finalizadas en Jira.
- `main` sincronizada con GitHub.
- Suite de tests pasando con 5 tests.

### Siguiente Paso

- Iniciar el nivel avanzado con refactorizacion a programacion orientada a objetos.

## Dia 3 - 11 de mayo de 2026

### Objetivos

- Empezar el nivel avanzado.
- Refactorizar el codigo usando programacion orientada a objetos.
- Mantener el flujo de trabajo con rama, tests, commit, Pull Request y merge.
- Revisar el codigo manualmente antes de avanzar a la siguiente funcionalidad.

### Trabajo Realizado

- Se partio desde `main` limpio y sincronizado.
- Se creo la rama `feature/oop-taximeter`.
- Se anadio la clase `Taximeter`.
- Se movio el estado del trayecto a atributos de instancia:
  - `trip_active`
  - `stopped_time`
  - `moving_time`
  - `state`
  - `state_start_time`
- Se implementaron los metodos:
  - `start_trip`
  - `change_state`
  - `finish_trip`
- Se actualizo el CLI para usar la clase `Taximeter`.
- Se eliminaron variables sueltas de la funcion `taximeter`.
- Se anadieron tests unitarios para validar el comportamiento principal de la clase.
- Se fusiono la rama mediante Pull Request.

### Validaciones

```bash
python -m py_compile taximetro.py
python -m pytest
git diff --check
```

Resultado:

```text
10 tests pasados
```

Prueba manual realizada:

- `finish` sin trayecto activo.
- `start`.
- segundo `start`.
- `move`.
- `stop`.
- `finish`.
- `exit`.

### Decisiones

- Centralizar la logica principal en la clase `Taximeter`.
- Mantener el CLI como capa de interaccion con el usuario.
- No iniciar la GUI hasta tener la logica mejor organizada.
- Ampliar los tests al introducir OOP.

### Problemas Y Aprendizajes

- Durante el refactor aparecieron errores de nombres de variables y llamadas a metodos.
- Algunos tests seguian pasando aunque el CLI fallaba, porque todavia no cubrian el flujo interactivo.
- Se hizo una revision manual del codigo y una prueba real del CLI antes del commit.
- Se limpiaron espacios sobrantes detectados por:

```bash
git diff --check
```

### Estado Actual

- Nivel esencial completado.
- Nivel medio completado.
- Primera tarea del nivel avanzado completada.
- 8 tareas finalizadas en Jira.
- `main` sincronizada con GitHub tras el Pull Request #7.
- Suite de tests pasando con 10 tests.

### Continuacion Del Dia

Despues de completar la refactorizacion con OOP, se continuo con varias tareas del nivel avanzado y con mejoras de documentacion.

#### Autenticacion Basica

Trabajo realizado:

- Se creo una rama especifica para autenticacion.
- Se amplio `config.json` para incluir la contrasena del programa.
- Se creo la funcion `load_password`.
- Se creo la funcion `authenticate_user`.
- El CLI paso a solicitar contrasena antes de mostrar el menu principal.
- Se configuro un limite de tres intentos.
- Se registraron en logs los accesos correctos y los intentos fallidos.
- Se anadio un test para validar la carga de contrasena.
- Se fusiono la funcionalidad mediante Pull Request.

Validaciones realizadas:

```bash
python -m py_compile taximetro.py
python -m pytest
python taximetro.py
```

Resultado:

```text
11 tests pasados
```

Pruebas manuales:

- Acceso correcto con `admin123`.
- Tres intentos fallidos.
- Registro de autenticacion correcta en `taximetro.log`.
- Registro de intentos fallidos en `taximetro.log`.

#### Documentacion Profesional

Trabajo realizado:

- Se reviso el estilo general del `README.md`.
- Se amplio la explicacion de instalacion, dependencias y ejecucion.
- Se documento el uso de `config.json`.
- Se documento el flujo de trabajo con ramas, commits, Pull Requests y sincronizacion de `main`.
- Se anadio una seccion de seguimiento del briefing separada por niveles.
- Se usaron checks visuales para mostrar requisitos completados, en curso y pendientes.

Decision:

- Mantener el README como documento principal para explicar el estado funcional del proyecto.
- Mantener el diario como documento de aprendizaje y trazabilidad del proceso.

#### Interfaz Grafica Con CustomTkinter

Trabajo realizado:

- Se creo la rama `feature/gui-customtkinter`.
- Se instalo `customtkinter`.
- Se actualizo `requirements.txt`.
- Se creo el archivo `gui.py`.
- Se diseno una primera interfaz grafica con:
  - pantalla de autenticacion,
  - panel de estado,
  - importe actual,
  - tiempo parado,
  - tiempo en movimiento,
  - configuracion visible,
  - ultimo trayecto,
  - botones de control.
- Se conecto la GUI con la clase `Taximeter`.
- Se anadio actualizacion visual de tiempos e importe durante el trayecto.
- Se anadio resaltado visual del boton de estado activo.
- Se anadio una banda destacada para mostrar el importe final.
- Se anadio una instruccion dinamica bajo los botones para orientar al usuario segun el estado del trayecto.

Estado:

- La GUI esta en desarrollo.
- Falta realizar una validacion final completa antes de cerrar la funcionalidad.
- Falta decidir si se fusiona la rama hoy o se deja abierta para revisarla al dia siguiente.

Validaciones pendientes:

```bash
python -m py_compile gui.py
python -m pytest
python gui.py
```

Pruebas manuales pendientes:

- Probar acceso correcto con `admin123`.
- Probar acceso incorrecto y bloqueo tras tres intentos.
- Probar `Iniciar`.
- Probar cambio a `Movimiento`.
- Probar cambio a `Parado`.
- Probar `Finalizar`.
- Comprobar que el importe final queda visible.
- Comprobar que el boton de estado activo se resalta correctamente.

### Estado Actual

- Nivel esencial completado.
- Nivel medio completado.
- Nivel avanzado en curso.
- OOP completado.
- Autenticacion basica completada.
- Documentacion principal mejorada.
- GUI iniciada con CustomTkinter.
- Rama actual de GUI pendiente de validacion final y commit.

### Siguiente Paso

- Validar la GUI.
- Hacer commit de `gui.py`, `requirements.txt` y `README.md` si la prueba es correcta.
- Actualizar Jira dejando la tarea de GUI como en curso o completada segun el resultado.

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
- Se anadio una luz de estado con parpadeo sutil cuando el taxi esta en movimiento.
- Se anadio una banda destacada para mostrar el importe final.
- Se anadio una instruccion dinamica bajo los botones para orientar al usuario segun el estado del trayecto.
- Se incorporo edicion de tarifas desde la GUI antes de iniciar el trayecto.
- Se mantuvo la restriccion de no cambiar tarifas durante un trayecto activo para evitar calculos inconsistentes.
- Se conecto la finalizacion desde GUI con el historico `trip_history.txt`.
- Se anadieron logs especificos para acciones realizadas desde la GUI.
- Se reforzo la validacion de estados en la clase `Taximeter`.
- Se anadio un test para rechazar estados invalidos.
- Se identifico como mejora futura un sistema de gestion de usuarios para sustituir la contrasena unica del MVP.

Validaciones realizadas:

```bash
python -m py_compile taximetro.py
python -m py_compile gui.py
python -m pytest
python gui.py
```

Resultado:

```text
12 tests pasados
```

Pruebas manuales realizadas:

- Probar acceso correcto con `admin123`.
- Probar acceso incorrecto y bloqueo tras tres intentos.
- Probar `Iniciar`.
- Probar cambio a `Movimiento`.
- Probar cambio a `Parado`.
- Probar `Finalizar`.
- Comprobar que el importe final queda visible.
- Comprobar que el boton de estado activo se resalta correctamente.
- Comprobar que las tarifas se pueden cambiar antes de iniciar un trayecto.
- Comprobar que no se pueden cambiar tarifas durante un trayecto activo.
- Comprobar que un trayecto finalizado desde la GUI se guarda en el historico.
- Comprobar que la luz de estado cambia segun el estado del trayecto.

#### Revision Profunda Del Proyecto

Antes de cerrar la GUI se realizo una revision general del proyecto frente al briefing.

Puntos revisados:

- Estructura del repositorio.
- Uso de entorno virtual `.venv`.
- Flujo de trabajo con ramas y Pull Requests.
- Estado del README.
- Estado del diario de desarrollo.
- Funcionalidad del CLI.
- Funcionalidad de la GUI.
- Configuracion de tarifas.
- Autenticacion.
- Logs.
- Historico de trayectos.
- Tests unitarios.
- Archivos ignorados en `.gitignore`.

Conclusiones:

- El nivel esencial queda completado.
- El nivel medio queda completado.
- El nivel avanzado queda completado.
- El nivel experto queda pendiente para la siguiente fase.
- La GUI mantiene coherencia funcional con el CLI: calcula tarifas, registra historico y genera logs.
- El proyecto conserva un flujo profesional basado en ramas, commits descriptivos, Pull Requests y validaciones.

Mejoras identificadas para fases futuras:

- Sustituir el historico en texto plano por SQLite.
- Dockerizar la aplicacion.
- Crear una version web.
- Evolucionar la autenticacion basica hacia un sistema de gestion de usuarios.

### Estado Actual

- Nivel esencial completado.
- Nivel medio completado.
- Nivel avanzado completado.
- OOP completado.
- Autenticacion basica completada.
- Documentacion principal mejorada.
- GUI completada con CustomTkinter.
- Suite ampliada a 12 tests.
- Rama actual de GUI pendiente de Pull Request y fusion en `main`.

### Siguiente Paso

- Actualizar Jira marcando la GUI y el nivel avanzado como completados.
- Abrir o actualizar el Pull Request de `feature/gui-customtkinter`.
- Fusionar la rama en `main`.
- Actualizar `main` local con `git pull origin main`.
- Iniciar el nivel experto con base de datos SQLite.

## Dia 4 - 12 de mayo de 2026

### Objetivos

- Iniciar el nivel experto del briefing.
- Integrar una base de datos SQLite para almacenar trayectos finalizados.
- Dockerizar la ejecucion del CLI.
- Mantener la separacion entre ejecucion local, GUI de escritorio y futura version web.
- Revisar la documentacion para reflejar el estado real del proyecto.

### Base De Datos SQLite

Trabajo realizado:

- Se creo la rama `feature/sqlite-database`.
- Se creo el modulo `database.py`.
- Se definio la base de datos local `taximetro.db`.
- Se creo la tabla `trips`.
- Se incorporo la funcion `init_database`.
- Se incorporo la funcion `save_trip_to_database`.
- Se incorporo la funcion `get_recent_trips`.
- Se integro el guardado en SQLite desde el CLI.
- Se integro el guardado en SQLite desde la GUI.
- Se mantuvo el historico en texto plano como salida complementaria.
- Se anadio `*.db` al `.gitignore`.
- Se anadieron tests unitarios para validar la creacion de la tabla y la insercion de trayectos.

Validaciones realizadas:

```bash
python -m py_compile database.py
python -m py_compile taximetro.py
python -m py_compile gui.py
python -m pytest
python taximetro.py
```

Resultado:

```text
14 tests pasados
```

Tambien se valido manualmente la lectura de registros desde SQLite:

```bash
python -c "import sqlite3; conn=sqlite3.connect('taximetro.db'); print(conn.execute('SELECT id, finished_at, stopped_time, moving_time, stopped_rate, moving_rate, total_fare FROM trips ORDER BY id DESC LIMIT 3').fetchall()); conn.close()"
```

Decision:

- Usar SQLite como primera base de datos porque es suficiente para el alcance del MVP, no requiere servidor externo y permite demostrar persistencia estructurada.

### Dockerizacion Del CLI

Trabajo realizado:

- Se creo la rama `feature/docker-CLI`.
- Se creo el archivo `Dockerfile`.
- Se creo el archivo `.dockerignore`.
- Se construyo la imagen `taximetro-cli`.
- Se valido la ejecucion interactiva del CLI dentro del contenedor.
- Se configuro `TAXIMETER_DATA_DIR=/app/data`.
- Se adapto la ruta de la base de datos para poder guardar datos dentro de `/app/data`.
- Se adapto la ruta del historico de trayectos para poder guardarlo dentro de `/app/data`.
- Se corrigio la configuracion de logs para usar la ruta `LOG_FILE` y respetar `TAXIMETER_DATA_DIR`.
- Se valido un volumen Docker llamado `taximetro_data`.
- Se comprobo que SQLite persiste datos dentro del volumen.

Validaciones realizadas:

```bash
python -m py_compile database.py
python -m py_compile taximetro.py
python -m pytest
docker build -t taximetro-cli .
winpty docker run --rm -it taximetro-cli
docker run --rm -it -v taximetro_data:/app/data taximetro-cli
docker volume ls
```

Consulta de validacion sobre el volumen:

```powershell
docker run --rm -v taximetro_data:/app/data taximetro-cli python -c "import sqlite3; conn=sqlite3.connect('/app/data/taximetro.db'); print(conn.execute('SELECT id, finished_at, total_fare FROM trips ORDER BY id DESC LIMIT 3').fetchall()); conn.close()"
```

Decisiones:

- Dockerizar el CLI como demostracion de portabilidad y ejecucion aislada.
- Mantener la GUI de escritorio como ejecucion local con CustomTkinter.
- Documentar que Docker Desktop no es la forma recomendada de arrancar este CLI, porque la aplicacion necesita una terminal interactiva conectada a `input()`.
- Recomendar PowerShell para las pruebas con volumen en Windows.
- Reservar una estrategia Docker especifica para la futura version web con Flask.

### Documentacion

Trabajo realizado:

- Se actualizo el `README.md`.
- Se corrigio el estado del nivel experto.
- Se documento SQLite.
- Se documento Docker.
- Se documentaron los comandos de build y ejecucion.
- Se documento la ejecucion con volumen persistente.
- Se documento la diferencia entre CLI dockerizado, GUI local y futura web.
- Se recupero una presentacion visual por niveles mediante badges de estado compatibles con GitHub.

### Problemas Y Aprendizajes

- Git Bash en Windows puede transformar rutas Linux como `/app/data` al usar volumenes Docker.
- Para el CLI interactivo en Git Bash fue necesario usar `winpty`.
- Para validar volumenes Docker en Windows resulto mas estable usar PowerShell.
- El boton `Run` de Docker Desktop no es adecuado para este caso porque no conecta correctamente la entrada interactiva que necesita `input()`.
- Se detecto una incoherencia en la configuracion de logs: aunque existia `LOG_FILE`, `logging.basicConfig` seguia apuntando a `taximetro.log` de forma literal. Se corrigio para respetar `TAXIMETER_DATA_DIR`.

### Estado Al Cierre

- Nivel esencial completado.
- Nivel medio completado.
- Nivel avanzado completado.
- SQLite completado dentro del nivel experto.
- Docker CLI completado dentro del nivel experto.
- Suite de tests pasando con 14 tests.
- Queda pendiente la version web accesible desde navegador.

### Siguiente Paso

- Disenar en Figma la experiencia de la version web.
- Implementar la aplicacion web con Flask.
- Reutilizar la logica existente del taximetro.
- Mostrar historico desde SQLite.
- Preparar las presentaciones tecnica y no tecnica.
## Dia 5 - 17 de mayo de 2026

### Objetivos

- Disenar la experiencia de la version web.
- Preparar una propuesta visual coherente con el producto.
- Implementar la aplicacion web con Flask.
- Conectar la web con la logica existente del taximetro.

### UX/UI En Figma

Trabajo realizado:

- Se creo un prototipo UX/UI en Figma para la version web.
- Se descarto una primera aproximacion demasiado similar a la GUI de escritorio.
- Se eligio un enfoque visual oscuro, sobrio y moderno, con inspiracion ligera en taximetros clasicos.
- Se definieron pantallas principales, componentes, flujo de usuario, diagramas de apoyo, persona y casos de uso.
- Se uso Figma como apoyo de diseno, no como requisito de ejecucion tecnica.

Enlace del prototipo:

```text
https://www.figma.com/design/hfzWUpKkCrJsnI5ToBfTcq/Tax%C3%ADmetro-Digital-F5---Prototipo-Web?m=auto&t=TDCuPRO36jeoOvQw-6
```

Decision:

- Mantener Figma como entregable de UX/UI y referencia visual para la web.
- No seguir iterando en Figma una vez validado el look general para ahorrar tiempo y centrar el cierre en funcionalidad, documentacion y entrega.

### Version Web Con Flask

Trabajo realizado:

- Se creo la rama `feature/flask-web`.
- Se instalo Flask y se actualizo `requirements.txt`.
- Se creo `app.py`.
- Se crearon las plantillas `login.html` y `dashboard.html`.
- Se creo `static/css/styles.css`.
- Se implemento login web usando la contrasena de `config.json`.
- Se creo un dashboard para iniciar, cambiar estado, finalizar y reiniciar trayectos.
- Se conecto la version web con SQLite para mostrar viajes registrados.
- Se anadio visualizacion de logs tecnicos recientes.
- Se permitio modificar tarifas antes de iniciar un trayecto.
- Se bloqueo la modificacion de tarifas durante trayecto activo.
- Se anadio indicador visual de estado: libre, ocupado, taxi parado, en movimiento y finalizado.
- Se corrigio el contador para actualizar tiempos e importe con JavaScript, sin recargar la pagina.

Validaciones realizadas:

```bash
python -m py_compile app.py
python -m pytest
git diff --check
python app.py
```

Resultado:

```text
14 tests pasados
```

Pruebas manuales:

- Login correcto.
- Inicio de trayecto.
- Cambio a movimiento.
- Cambio a parado.
- Finalizacion del trayecto.
- Reinicio con nuevo viaje.
- Visualizacion de viajes en SQLite.
- Visualizacion de logs recientes.
- Cambio de tarifas antes de iniciar.

### Estado Al Cierre

- Prototipo Figma completado.
- Version web Flask completada.
- La web queda conectada con SQLite, logs y configuracion.
- Queda pendiente dockerizar la web y cerrar documentacion final.

## Dia 6 - 18 de mayo de 2026

### Objetivos

- Dockerizar la version web.
- Validar persistencia de datos en Docker.
- Revisar el estado final del proyecto frente al briefing.
- Preparar documentacion de cierre para la entrega.

### Docker Web

Trabajo realizado:

- Se creo la rama `feature/docker-web`.
- Se creo `Dockerfile.web` para la aplicacion Flask.
- Se configuro Flask para escuchar en `0.0.0.0` dentro del contenedor.
- Se expuso el puerto `5000`.
- Se construyo la imagen `taximetro-web`.
- Se ejecuto la web dentro del contenedor.
- Se valido el acceso desde `http://localhost:5000`.
- Se probo persistencia con el volumen `taximetro_web_data`.

Validaciones realizadas:

```bash
python -m py_compile app.py
python -m pytest
git diff --check
docker build -f Dockerfile.web -t taximetro-web .
docker run --rm -p 5000:5000 -v taximetro_web_data:/app/data taximetro-web
```

Resultado:

```text
14 tests pasados
```

Prueba manual de persistencia:

- Se arranco el contenedor con volumen.
- Se registro un trayecto desde la web.
- Se detuvo el contenedor.
- Se arranco de nuevo con el mismo volumen.
- Se comprobo que el viaje seguia apareciendo en la tabla.

### Revision Tecnica

Puntos revisados:

- CLI funcional.
- GUI funcional.
- Web funcional.
- SQLite integrada.
- Logs generados correctamente.
- Historico en texto plano generado correctamente.
- Docker CLI validado.
- Docker web validado.
- Persistencia con volumen validada.
- `.gitignore` protege `.venv`, caches, logs, base de datos e historico generado.
- Tests unitarios pasando.

Comandos de revision:

```bash
git status
python -m pytest
python -m py_compile taximetro.py
python -m py_compile database.py
python -m py_compile app.py
python -m py_compile gui.py
git diff --check
git status --ignored
```

Conclusiones:

- El nivel esencial queda completado.
- El nivel medio queda completado.
- El nivel avanzado queda completado.
- El nivel experto queda completado.
- El proyecto queda tecnicamente preparado para entrega.
- Quedan pendientes las presentaciones y el guion personal de defensa.

### Cierre De Documentacion

Trabajo realizado:

- Se reviso el README para convertirlo en documento principal de entrega.
- Se anadieron entregables, tecnologias, instalacion, ejecucion, Docker, base de datos, arquitectura, UX/UI y mejoras futuras.
- Se dejaron huecos para enlazar las presentaciones cuando esten preparadas.
- Se actualizo el diario con Figma, Flask, Docker web y revision tecnica final.

### Siguiente Paso

- Preparar presentacion para publico no tecnico.
- Preparar presentacion tecnica.
- Preparar guion personal de defensa de 5 minutos.
- Realizar revision final del repositorio y entregar.

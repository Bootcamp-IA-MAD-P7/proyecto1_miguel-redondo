# Diario de desarrollo

## Dia 1 - 7 de mayo de 2026

### Objetivos del dia

- Crear el repositorio oficial del proyecto en la organizacion del bootcamp.
- Preparar el proyecto en local.
- Configurar un entorno virtual aislado.
- Subir el codigo base del taximetro.
- Crear una rama de trabajo para el nivel esencial.
- Probar el funcionamiento inicial del CLI.
- Crear el tablero Kanban en Jira.
- Empezar a mejorar la experiencia de uso del CLI.

### Trabajo realizado

- Se creo el repositorio `proyecto1_miguel-redondo` en la organizacion `Bootcamp-IA-MAD-P7`.
- Se creo la carpeta local del proyecto dentro de `Bootcamp-FactoriaF5`.
- Se configuro el entorno virtual `.venv` dentro del proyecto.
- Se creo el archivo `.gitignore` para ignorar `.venv/` y `__pycache__/`.
- Se anadio el codigo base en `taximetro.py`.
- Se creo un `README.md` inicial.
- Se subio la rama `main` al repositorio remoto.
- Se creo la rama `feature/nivel-esencial`.
- Se probo el flujo inicial del programa: iniciar, mover, parar, finalizar y salir.
- Se elimino un mensaje de depuracion del calculo de tarifa.
- Se extrajeron las tarifas a constantes (`STOPPED_RATE` y `MOVING_RATE`).
- Se mejoraron los mensajes del CLI en espanol.
- Se subieron los cambios a GitHub.
- Se creo un tablero Jira para gestionar el proyecto.

### Decisiones tomadas

- Usar Git Bash para los comandos del proyecto.
- Usar VSCode para editar archivos.
- Usar un entorno virtual `.venv` dentro del proyecto.
- No trabajar directamente sobre `main`.
- Usar ramas de tipo `feature/...` para desarrollar funcionalidades.
- Mantener commits pequenos y descriptivos con estilo Conventional Commits.
- Usar Jira como tablero Kanban para simular una gestion profesional del proyecto.

### Problemas encontrados

- Al importar el modulo aparecio la carpeta `__pycache__/`.
- Se soluciono anadiendo `__pycache__/` al `.gitignore`.
- Durante una prueba, un cambio incompleto en `calculate_fare` provoco que la funcion devolviera `None`.
- Se corrigio la funcion y se valido con una prueba directa:

```bash
python -c "from taximetro import calculate_fare; print(calculate_fare(10, 5))"
```

### Estado al final del dia

- Repositorio creado y subido a GitHub.
- Entorno virtual configurado.
- Rama `feature/nivel-esencial` creada y subida.
- CLI funcional y probado.
- Jira iniciado con tareas del proyecto.
- Documentacion inicial actualizada.

### Siguiente paso

- Completar el nivel esencial del CLI.
- Revisar y ampliar el README.
- Avanzar hacia el nivel medio: logs, tests, historico en archivo y configuracion de tarifas.

## Dia 2 - 8 de mayo de 2026

### Objetivos del dia

- Continuar desde `main` limpio y sincronizado.
- Completar las tareas del nivel medio.
- Mantener el flujo profesional con ramas, commits, Pull Requests y Jira.
- Seguir entendiendo cada cambio antes de implementarlo.

### Trabajo realizado

- Se implemento el sistema de logs en la rama `feature/logs`.
- Se registraron eventos principales con `INFO`.
- Se registraron usos incorrectos con `WARNING`.
- Se anadio `*.log` al `.gitignore`.
- Se creo Pull Request y se fusiono en `main`.
- Se anadieron tests unitarios en la rama `feature/tests-unitarios`.
- Se instalo `pytest` dentro del entorno virtual.
- Se creo `requirements.txt`.
- Se creo la carpeta `tests/` y el archivo `tests/test_taximetro.py`.
- Se validaron casos de calculo de tarifa con tiempo parado, tiempo en movimiento, ambos tiempos y trayecto sin tiempo.
- Se creo Pull Request y se fusiono en `main`.
- Se implemento el historico de trayectos en la rama `feature/historico-trayectos`.
- Se creo la funcion `save_trip_history`.
- Se guardan trayectos finalizados en `trip_history.txt`.
- Se anadio `trip_history.txt` al `.gitignore`.
- Se creo Pull Request y se fusiono en `main`.
- Se implemento la configuracion de tarifas en la rama `feature/configuracion-tarifas`.
- Se creo `config.json`.
- Se creo la funcion `load_rates`.
- `calculate_fare` ahora acepta tarifas configurables.
- Se anadio un test para tarifas personalizadas.
- Se creo Pull Request y se fusiono en `main`.

### Validaciones realizadas

- `python -m py_compile taximetro.py`
- `python taximetro.py`
- `python -m pytest`
- Revision manual de `taximetro.log`.
- Revision manual de `trip_history.txt`.
- Prueba manual modificando temporalmente `config.json`.

### Decisiones tomadas

- Mantener `main` como rama estable.
- Crear una rama por cada tarea importante.
- Fusionar mediante Pull Request despues de probar.
- No subir archivos generados localmente como logs o historicos.
- Usar `config.json` para que las tarifas puedan cambiar sin modificar codigo.
- Usar `pytest` como herramienta de testing.
- Documentar al final del dia para no perder ritmo durante el desarrollo.

### Problemas encontrados

- Al ejecutar `py_compile`, un error de escritura en el comando impidio encontrar el modulo.
- Se corrigio usando `python -m py_compile taximetro.py`.
- En la configuracion de tarifas, `load_rates` devolvia `None` porque faltaba `return stopped_rate, moving_rate`.
- Se corrigio la funcion y se verifico el arranque del programa.
- Se detecto que el `print` de tarifas necesitaba ser f-string para mostrar los valores reales.
- Se corrigieron pequenos detalles de texto antes de validar.

### Estado al final del dia

- Nivel esencial completado.
- Nivel medio completado.
- 7 tareas finalizadas en Jira.
- `main` sincronizada con GitHub.
- Tests pasando: 5 tests.
- Proyecto listo para empezar el nivel avanzado.

### Siguiente paso

- Iniciar el nivel avanzado con la refactorizacion a programacion orientada a objetos.


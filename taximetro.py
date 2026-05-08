import json
import logging
import time
from datetime import datetime

STOPPED_RATE = 0.02
MOVING_RATE = 0.05
HISTORY_FILE = "trip_history.txt"
CONFIG_FILE = "config.json"

def load_rates():
    """
    Carga las tarifas desde un archivo de configuracion.
    Si el archivo no existe o falla, usa las tarifas por defecto.
    """
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            config = json.load(file)

        stopped_rate = config.get("stopped_rate", STOPPED_RATE)
        moving_rate = config.get("moving_rate", MOVING_RATE)
        return stopped_rate, moving_rate

    except FileNotFoundError:
        logging.warning("Archivo de configuracion no encontrado. Se usan las tarifas por defecto.")
        return STOPPED_RATE, MOVING_RATE

# Configuracion del sistema de logs
logging.basicConfig(
    filename="taximetro.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def calculate_fare(seconds_stopped, seconds_moving, stopped_rate=STOPPED_RATE, moving_rate=MOVING_RATE):
    """
    Calcula la tarifa total en euros.
    """
    fare = seconds_stopped * stopped_rate + seconds_moving * moving_rate
    return fare

def save_trip_history(stopped_time, moving_time, total_fare):
    """
    Guarda un trayecto finalizado en un archivo de texto.
    """
    finished_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = (
        f"{finished_at} | "
        f"parado: {stopped_time:.1f}s | "
        f"movimiento: {moving_time:.1f}s | "
        f"total: {total_fare:.2f} euros\n"
    )

    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(line)

def taximeter():
    """
    Funcion para manejar y mostrar las opciones del taximetro.
    """
    logging.info("Programa iniciado")
    stopped_rate, moving_rate = load_rates()
    logging.info(f"Tarifas cargadas: parado={stopped_rate}, movimiento={moving_rate}")
    print("Bienvenido al Taximetro Digital F5")
    print("Este programa calcula el importe de un trayecto segun el tiempo parado y en movimiento.")
    print(f"Tarifas: parado = {stopped_rate} euros/segundo | movimiento = {moving_rate} euros/segundo")
    print("Comandos disponibles:")
    print("  start  - iniciar un trayecto")
    print("  stop   - indicar que el taxi esta parado")
    print("  move   - indicar que el taxi esta en movimiento")
    print("  finish - finalizar el trayecto y mostrar el total")
    print("  exit   - salir del programa\n")

    trip_active = False
    start_time = 0
    stopped_time = 0
    moving_time = 0
    state = None  # 'stopped' o 'moving'
    state_start_time = 0

    while True:
        command = input("> ").strip().lower()

        if command == "start":
            if trip_active:
                logging.warning("Intento de iniciar un trayecto cuando ya habia uno activo")
                print("Error: ya hay un trayecto en curso.")
                continue
            trip_active = True
            start_time = time.time()
            stopped_time = 0
            moving_time = 0
            state = 'stopped'  # Iniciamos en estado 'stopped'
            state_start_time = time.time()
            logging.info("Trayecto iniciado")
            print("Trayecto iniciado. Estado inicial: parado.")

        elif command in ("stop", "move"):
            if not trip_active:
                logging.warning(f"Intento de cambiar a '{command}' sin trayecto activo")
                print("Error: no hay ningun trayecto activo. Usa 'start' primero.")
                continue
            # Calcula el tiempo del estado anterior
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration

            # Cambia el estado
            state = 'stopped' if command == "stop" else 'moving'
            state_start_time = time.time()
            state_label = "parado" if state == 'stopped' else "en movimiento"
            logging.info(f"Estado actualizado: {state_label}")
            print(f"Estado actualizado: {state_label}.")

        elif command == "finish":
            if not trip_active:
                logging.warning("Intento de finalizar sin trayecto activo")
                print("Error: no hay ningun trayecto activo para finalizar.")
                continue
            # Agrega tiempo del ultimo estado
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration

            # Calcula la tarifa total y muestra el resumen del viaje
            total_fare = calculate_fare(stopped_time, moving_time, stopped_rate, moving_rate)
            logging.info(
                f"Trayecto finalizado. Tiempo parado: {stopped_time:.1f}s, "
                f"tiempo en movimiento: {moving_time:.1f}s, total: {total_fare:.2f} euros"
            )
            save_trip_history(stopped_time, moving_time, total_fare)
            print(f"\n--- Resumen del trayecto ---")
            print(f"Tiempo parado: {stopped_time:.1f} segundos")
            print(f"Tiempo en movimiento: {moving_time:.1f} segundos")
            print(f"Importe total: {total_fare:.2f} euros")
            print("----------------------------\n")

            # Reset las variables para el proximo viaje
            trip_active = False
            state = None

        elif command == "exit":
            logging.info("Programa finalizado")
            print("Saliendo del programa. Hasta pronto.")
            break

        else:
            print("Comando no reconocido. Usa: start, stop, move, finish o exit.")

if __name__ == "__main__":
    taximeter()

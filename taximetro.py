import json
import logging
import time
from datetime import datetime

STOPPED_RATE = 0.02
MOVING_RATE = 0.05
HISTORY_FILE = "trip_history.txt"
CONFIG_FILE = "config.json"
VALID_STATES = ("stopped", "moving")

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

    except (FileNotFoundError, json.JSONDecodeError):
        logging.warning("No se pudo cargar la configuracion. Se usan las tarifas por defecto.")
        return STOPPED_RATE, MOVING_RATE

def load_password():
    """
    Carga la contrasena desde el archivo de configuracion.
    """
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            config = json.load(file)

        return config.get("password", "admin123")

    except (FileNotFoundError, json.JSONDecodeError):
        logging.warning("No se pudo cargar la configuracion. Se usa contrasena por defecto.")
        return "admin123"

def authenticate_user(max_attempts=3):
    """
    Solicita la contrasena antes de permitir el acceso al programa.
    """
    expected_password = load_password()

    for attempt in range(max_attempts):
        password = input("Introduce la contrasena: ").strip()

        if password == expected_password:
            logging.info("Autenticacion correcta")
            print("Acceso concedido.\n")
            return True

        logging.warning("Intento de autenticacion fallido")
        remaining_attempts = max_attempts - attempt - 1

        if remaining_attempts > 0:
            print(f"Contrasena incorrecta. Intentos restantes: {remaining_attempts}")

    print("Acceso denegado.")
    return False

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

class Taximeter:
    """
    Representa el estado y las operaciones principales del taximetro.
    """

    def __init__(self, stopped_rate=STOPPED_RATE, moving_rate=MOVING_RATE):
        self.stopped_rate = stopped_rate
        self.moving_rate = moving_rate
        self.trip_active = False
        self.stopped_time = 0
        self.moving_time = 0
        self.state = None
        self.state_start_time = 0

    def start_trip(self):
        """
        Inicia un nuevo trayecto.
        """
        if self.trip_active:
            return False
        self.trip_active = True
        self.stopped_time = 0
        self.moving_time = 0
        self.state = "stopped"
        self.state_start_time = time.time()
        return True

    def change_state(self, new_state):
        """
        Cambia el estado del taxi y acumula el tiempo del estado anterior.
        """
        if not self.trip_active:
            return False

        if new_state not in VALID_STATES:
            return False

        duration = time.time() - self.state_start_time

        if self.state == "stopped":
            self.stopped_time += duration
        else:
            self.moving_time += duration

        self.state = new_state
        self.state_start_time = time.time()
        return True

    def finish_trip(self):
        """
        Finaliza el trayecto activo y devuelve un resumen.
        """
        if not self.trip_active:
            return None
        duration = time.time() - self.state_start_time

        if self.state == "stopped":
            self.stopped_time += duration
        else:
            self.moving_time += duration

        total_fare = calculate_fare(
            self.stopped_time,
            self.moving_time,
            self.stopped_rate,
            self.moving_rate
        )

        summary = {
            "stopped_time": self.stopped_time,
            "moving_time": self.moving_time,
            "total_fare": total_fare
        }

        self.trip_active = False
        self.state = None
        self.state_start_time = 0

        return summary

def taximeter():
    """
    Funcion para manejar y mostrar las opciones del taximetro.
    """
    logging.info("Programa iniciado")

    if not authenticate_user():
        logging.warning("Programa finalizado por fallo de autenticacion")
        return

    stopped_rate, moving_rate = load_rates()
    logging.info(f"Tarifas cargadas: parado={stopped_rate}, movimiento={moving_rate}")
    taximeter_app = Taximeter(stopped_rate, moving_rate)
    print("Bienvenido al Taximetro Digital F5")
    print("Este programa calcula el importe de un trayecto segun el tiempo parado y en movimiento.")
    print(f"Tarifas: parado = {stopped_rate} euros/segundo | movimiento = {moving_rate} euros/segundo")
    print("Comandos disponibles:")
    print("  start  - iniciar un trayecto")
    print("  stop   - indicar que el taxi esta parado")
    print("  move   - indicar que el taxi esta en movimiento")
    print("  finish - finalizar el trayecto y mostrar el total")
    print("  exit   - salir del programa\n")

    while True:
        command = input("> ").strip().lower()

        if command == "start":
            if not taximeter_app.start_trip():
                logging.warning("Intento de iniciar un trayecto cuando ya habia uno activo")
                print("Error: ya hay un trayecto en curso.")
                continue

            logging.info("Trayecto iniciado")
            print("Trayecto iniciado. Estado inicial: parado.")

        elif command in ("stop", "move"):
            new_state = "stopped" if command == "stop" else "moving"

            if not taximeter_app.change_state(new_state):
                logging.warning(f"Intento de cambiar a '{command}' sin trayecto activo")
                print("Error: no hay ningun trayecto activo. Usa 'start' primero.")
                continue

            state_label = "parado" if new_state == "stopped" else "en movimiento"
            logging.info(f"Estado actualizado: {state_label}")
            print(f"Estado actualizado: {state_label}.")

        elif command == "finish":
            summary = taximeter_app.finish_trip()

            if summary is None:
                logging.warning("Intento de finalizar sin trayecto activo")
                print("Error: no hay ningun trayecto activo para finalizar.")
                continue

            stopped_time = summary["stopped_time"]
            moving_time = summary["moving_time"]
            total_fare = summary["total_fare"]

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

        elif command == "exit":
            logging.info("Programa finalizado")
            print("Saliendo del programa. Hasta pronto.")
            break

        else:
            print("Comando no reconocido. Usa: start, stop, move, finish o exit.")

if __name__ == "__main__":
    taximeter()

import time

STOPPED_RATE = 0.02
MOVING_RATE = 0.05

def calculate_fare(seconds_stopped, seconds_moving):
    """
    Calcula la tarifa total en euros.
    - Parado: 0.02 euros/segundo
    - En movimiento: 0.05 euros/segundo
    """
    fare = seconds_stopped * STOPPED_RATE + seconds_moving * MOVING_RATE
    return fare

def taximeter():
    """
    Funcion para manejar y mostrar las opciones del taximetro.
    """
    print("Bienvenido al Taximetro Digital F5")
    print("Este programa calcula el importe de un trayecto segun el tiempo parado y en movimiento.")
    print("Tarifas: parado = 0.02 euros/segundo | movimiento = 0.05 euros/segundo")
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
                print("Error: ya hay un trayecto en curso.")
                continue
            trip_active = True
            start_time = time.time()
            stopped_time = 0
            moving_time = 0
            state = 'stopped'  # Iniciamos en estado 'stopped'
            state_start_time = time.time()
            print("Trayecto iniciado. Estado inicial: parado.")

        elif command in ("stop", "move"):
            if not trip_active:
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
            print(f"Estado actualizado: {state_label}.")

        elif command == "finish":
            if not trip_active:
                print("Error: no hay ningun trayecto activo para finalizar.")
                continue
            # Agrega tiempo del ultimo estado
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration

            # Calcula la tarifa total y muestra el resumen del viaje
            total_fare = calculate_fare(stopped_time, moving_time)
            print(f"\n--- Resumen del trayecto ---")
            print(f"Tiempo parado: {stopped_time:.1f} segundos")
            print(f"Tiempo en movimiento: {moving_time:.1f} segundos")
            print(f"Importe total: {total_fare:.2f} euros")
            print("----------------------------\n")

            # Reset las variables para el proximo viaje
            trip_active = False
            state = None

        elif command == "exit":
            print("Saliendo del programa. Hasta pronto.")
            break

        else:
            print("Comando no reconocido. Usa: start, stop, move, finish o exit.")

if __name__ == "__main__":
    taximeter()

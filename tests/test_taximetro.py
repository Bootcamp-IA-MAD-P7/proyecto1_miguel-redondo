from taximetro import Taximeter, calculate_fare

def test_calculate_fare_with_stopped_and_moving_time():
    # Verifica la tarifa cuando hay tiempo parado y tiempo en movimiento.
    result = calculate_fare(10, 5)

    assert result == 0.45

def test_calculate_fare_with_only_stopped_time():
    # Verifica que solo se cobra la tarifa de tiempo parado.
    result = calculate_fare(10, 0)

    assert result == 0.20

def test_calculate_fare_with_only_moving_time():
    # Verifica que solo se cobra la tarifa de tiempo en movimiento.
    result = calculate_fare(0, 10)

    assert result == 0.50


def test_calculate_fare_without_time():
    # Verifica que un trayecto sin tiempo registrado tiene coste cero.
    result = calculate_fare(0, 0)

    assert result == 0

def test_calculate_fare_with_custom_rates():
    # Verifica que se pueden usar tarifas configurables.
    result = calculate_fare(10, 5, stopped_rate=0.10, moving_rate=0.20)

    assert result == 2.0

def test_taximeter_starts_without_active_trip():
    # Verifica que un taximetro nuevo empieza sin trayecto activo.
    taximeter = Taximeter()

    assert taximeter.trip_active is False
    assert taximeter.stopped_time == 0
    assert taximeter.moving_time == 0
    assert taximeter.state is None

def test_taximeter_start_trip_activates_trip():
    # Verifica que start_trip inicia un trayecto correctamente.
    taximeter = Taximeter()

    result = taximeter.start_trip()

    assert result is True
    assert taximeter.trip_active is True
    assert taximeter.state == "stopped"

def test_taximeter_cannot_start_trip_twice():
    # Verifica que no se puede iniciar un trayecto si ya hay uno activo.
    taximeter = Taximeter()

    first_result = taximeter.start_trip()
    second_result = taximeter.start_trip()

    assert first_result is True
    assert second_result is False


def test_taximeter_finish_without_active_trip_returns_none():
    # Verifica que no se puede finalizar si no hay trayecto activo.
    taximeter = Taximeter()

    result = taximeter.finish_trip()

    assert result is None

def test_taximeter_finish_trip_returns_summary():
    # Verifica que finalizar un trayecto devuelve un resumen con los datos esperados.
    taximeter = Taximeter()

    taximeter.start_trip()
    summary = taximeter.finish_trip()

    assert summary is not None
    assert "stopped_time" in summary
    assert "moving_time" in summary
    assert "total_fare" in summary
    assert taximeter.trip_active is False
    assert taximeter.state is None

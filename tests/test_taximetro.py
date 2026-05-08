from taximetro import calculate_fare

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
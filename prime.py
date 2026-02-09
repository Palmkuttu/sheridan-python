import pytest

def generate_prime_factors(number: int) -> list[int]:
    """Generates a list of prime factors for a given integer."""
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

    factors = []
    divisor = 2
    temp_number = number
    while temp_number > 1:
        while temp_number % divisor == 0:
            factors.append(divisor)
            temp_number //= divisor
        divisor += 1
    return factors

def test_input_non_integer():
    with pytest.raises(ValueError):
        generate_prime_factors("string")

    with pytest.raises(ValueError):
        generate_prime_factors(3.14)

def test_input_1_returns_empty():
    assert generate_prime_factors(1) == []

def test_input_2_returns_2():
    assert generate_prime_factors(2) == [2]

def test_input_3_returns_3():
    assert generate_prime_factors(3) == [3]

def test_input_4_returns_2_2():
    assert generate_prime_factors(4) == [2, 2]

def test_input_5_returns_2_3():
    assert generate_prime_factors(6) == [2, 3]

def test_input_6_returns_2_2_2():
    assert generate_prime_factors(8) == [2, 2, 2]

def test_input_7_returns_3_3():
    assert generate_prime_factors(9) == [3, 3]
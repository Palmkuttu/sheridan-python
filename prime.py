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


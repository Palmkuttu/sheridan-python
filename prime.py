
import pytest

def test_non_integer():
  with pytest.raises(ValueError):
    generate_prime_factors("abc")

def test_one():
    assert generate_prime_factors(1) == [1]

def test_two():
    assert generate_prime_factors(2) == [2]

def test_three():
    assert generate_prime_factors(3) == [3]
    assert generate_prime_factors(4) == [4]

def test_four():
    assert generate_prime_factors(4) == [4]
    assert generate_prime_factors(5) == [5]

def test_five():
    assert generate_prime_factors(5) == [5]
    assert generate_prime_factors(6) == [6]
    assert generate_prime_factors(7) == [7]

def test_six():
  assert generate_prime_factors(6) == [6]
  assert generate_prime_factors(7) == [7]
  assert generate_prime_factors(8) == [8]
  assert generate_prime_factors(9) == [9]

def test_seven():
  assert generate_prime_factors(7) == [7]
  assert generate_prime_factors(8) == [8]
  assert generate_prime_factors(9) == [9]

def test_eight():
  assert generate_prime_factors(8) == [8]
  assert generate_prime_factors(9) == [9]
  assert generate_prime_factors(10) == [10]

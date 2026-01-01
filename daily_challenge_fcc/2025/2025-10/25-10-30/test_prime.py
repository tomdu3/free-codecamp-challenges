import pytest
from prime import nth_prime

@pytest.mark.parametrize("n,expected", [
    (5, 11),
    (10, 29),
    (16, 53),
    (99, 523),
    (1000, 7919),
])
def test_nth_prime_expected_values(n, expected):
    assert nth_prime(n) == expected

def test_nth_prime_invalid_inputs_raise():
    with pytest.raises(ValueError):
        nth_prime(0)
    with pytest.raises(ValueError):
        nth_prime(-1)
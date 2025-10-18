import pytest
from missing_socks import sock_pairs

@pytest.mark.parametrize("pairs, cycles, expected", [
    (2, 5, 1),
    (1, 2, 0),
    (5, 11, 4),
    (6, 25, 3),
    (1, 8, 0),
])
def test_sock_pairs_examples(pairs, cycles, expected):
    assert sock_pairs(pairs, cycles) == expected
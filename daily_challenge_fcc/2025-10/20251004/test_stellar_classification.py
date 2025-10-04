from stellar_classification import classification

import pytest


@pytest.mark.parametrize("temp,expected", [
    (5778, "G"),
    (2400, "M"),
    (9999, "A"),
    (3700, "K"),
    (3699, "M"),
    (210000, "O"),
    (6000, "F"),
    (11432, "B"),
])
def test_classification_examples(temp, expected):
    assert classification(temp) == expected


import pytest
from credit_card_masker import mask

@pytest.mark.parametrize("card,expected", [
    ("4012-8888-8888-1881", "****-****-****-1881"),
    ("5105 1051 0510 5100", "**** **** **** 5100"),
    ("6011 1111 1111 1117", "**** **** **** 1117"),
    ("2223-0000-4845-0010", "****-****-****-0010"),
])
def test_mask_various_formats(card, expected):
    assert mask(card) == expected
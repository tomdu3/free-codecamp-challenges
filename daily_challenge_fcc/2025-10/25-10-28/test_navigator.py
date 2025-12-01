import pytest
from navigator import navigate

@pytest.mark.parametrize("commands,expected", [
    (["Visit About Us", "Back", "Forward"], "About Us"),
    (["Forward"], "Home"),
    (["Back"], "Home"),
    (["Visit About Us", "Visit Gallery"], "Gallery"),
    (["Visit About Us", "Visit Gallery", "Back", "Back"], "Home"),
    (["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"], "Contact"),
    (["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"], "Visit Us"),
])
def test_navigate(commands, expected):
    assert navigate(commands) == expected
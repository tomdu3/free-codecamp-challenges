import unittest
from extension_extractor import get_extension

"""
    Tests
Waiting:1. get_extension("document.txt") should return "txt".
Waiting:2. get_extension("README") should return "none".
Waiting:3. get_extension("image.PNG") should return "PNG".
Waiting:4. get_extension(".gitignore") should return "gitignore".
Waiting:5. get_extension("archive.tar.gz") should return "gz".
Waiting:6. get_extension("final.draft.") should return "none".
"""


def test_get_extension():
    assert get_extension("document.txt") == "txt"
    assert get_extension("README") == "none"
    assert get_extension("image.PNG") == "PNG"
    assert get_extension(".gitignore") == "gitignore"
    assert get_extension("archive.tar.gz") == "gz"
    assert get_extension("final.draft.") == "none"


if __name__ == "__main__":
    test_get_extension()

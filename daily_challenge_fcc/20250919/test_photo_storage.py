import pytest
from photo_storage import number_of_photos

def test_number_of_photos_basic():
    assert number_of_photos(1, 1) == 1000
    assert number_of_photos(2, 1) == 500
    assert number_of_photos(4, 256) == 64000
    assert number_of_photos(3.5, 750) == 214285
    assert number_of_photos(3.5, 5.5) == 1571

def test_number_of_photos_zero_photo_size():
    with pytest.raises(ZeroDivisionError):
        number_of_photos(0, 10)

def test_number_of_photos_zero_drive_size():
    assert number_of_photos(2, 0) == 0

def test_number_of_photos_large_drive_small_photo():
    assert number_of_photos(0.5, 1000) == 2000000

def test_number_of_photos_photo_larger_than_drive():
    assert number_of_photos(2000, 1) == 0

def test_number_of_photos_float_inputs():
    assert number_of_photos(2.5, 10.5) == 4200

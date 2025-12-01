import pytest
from file_storage import number_of_files

def test_number_of_files_kb():
    assert number_of_files(500, "KB", 1) == 2000

def test_number_of_files_b():
    assert number_of_files(50000, "B", 1) == 20000

def test_number_of_files_mb():
    assert number_of_files(5, "MB", 1) == 200

def test_number_of_files_b_fractional_drive():
    assert number_of_files(4096, "B", 1.5) == 366210

def test_number_of_files_kb_large_drive():
    assert number_of_files(220.5, "KB", 100) == 453514

def test_number_of_files_mb_large_drive():
    assert number_of_files(4.5, "MB", 750) == 166666
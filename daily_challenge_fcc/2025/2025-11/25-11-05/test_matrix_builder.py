from matrix_builder import build_matrix
import pytest


class TestMatrixBuilder:
    def test_build_matrix(self):
        assert build_matrix(2, 3) == [[0, 0, 0], [0, 0, 0]]
        assert build_matrix(3, 2) == [[0, 0], [0, 0], [0, 0]]
        assert build_matrix(4, 3) == [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        assert build_matrix(9, 1) == [[0], [0], [0], [0], [0], [0], [0], [0], [0]]



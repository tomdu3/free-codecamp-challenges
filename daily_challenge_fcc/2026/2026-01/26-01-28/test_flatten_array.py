from flatten_array import flatten_array
import unittest


class TestFlattenArray(unittest.TestCase):
    def test_flatten_array(self):
        self.assertEqual(flatten_array([1, [2, 3], 4]), [1, 2, 3, 4])
        self.assertEqual(flatten_array([5, [4, [3, 2]], 1]), [5, 4, 3, 2, 1])
        self.assertEqual(flatten_array(["A", [[[["B"]]]], "C"]), ["A", "B", "C"])
        self.assertEqual(
            flatten_array(
                [
                    ["L", "M", "N"],
                    ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]],
                    "V",
                    ["W", ["X", ["Y", ["Z"]]]],
                ]
            ),
            ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
        )
        self.assertEqual(
            flatten_array(
                [
                    ["red", ["blue", ["green", ["yellow", ["purple"]]]]],
                    "orange",
                    ["pink", ["brown"]],
                ]
            ),
            ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"],
        )


if __name__ == "__main__":
    unittest.main()

from inventory_update import update_inventory
import unittest 


class TestInventoryUpdate(unittest.TestCase):
    def test_inventory_update(self):
        self.assertEqual(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]]), [[3, "apples"], [8, "bananas"]])
        self.assertEqual(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]]), [[3, "apples"], [8, "bananas"], [4, "oranges"]])
        self.assertEqual(update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]]), [[10, "apples"], [30, "bananas"], [20, "oranges"]])
        self.assertEqual(update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]), [[1, "Bowling Ball"], [0, "Dirty Socks"], [1, "Hair Pin"], [0, "Microphone"], [1, "Half-Eaten Apple"], [1, "Toothpaste"]])


if __name__ == "__main__":
    unittest.main()

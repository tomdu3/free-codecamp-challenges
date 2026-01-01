from hex_generator import generate_hex
import unittest


import unittest
from hex_generator import generate_hex

class TestHexGenerator(unittest.TestCase):
    
    def test_1_invalid_color(self):
        """Test 1: generate_hex("yellow") should return "Invalid color"."""
        result = generate_hex("yellow")
        self.assertEqual(result, "Invalid color")
    
    def test_2_red_six_characters(self):
        """Test 2: generate_hex("red") should return a six-character string."""
        result = generate_hex("red")
        self.assertEqual(len(result), 6)
    
    def test_3_red_valid_hex(self):
        """Test 3: generate_hex("red") should return a valid six-character hex color code."""
        result = generate_hex("red")
        # Check all characters are valid hex digits (uppercase as per example)
        valid_chars = set("0123456789ABCDEF")
        self.assertTrue(all(c in valid_chars for c in result))
        self.assertEqual(len(result), 6)
    
    def test_4_red_dominant(self):
        """Test 4: generate_hex("red") should return a valid hex color with a higher red value than other colors."""
        result = generate_hex("red")
        r = int(result[0:2], 16)
        g = int(result[2:4], 16)
        b = int(result[4:6], 16)
        self.assertGreater(r, g, f"Red ({r}) should be greater than green ({g})")
        self.assertGreater(r, b, f"Red ({r}) should be greater than blue ({b})")
    
    def test_5_red_random_and_dominant(self):
        """Test 5: Calling generate_hex("red") twice should return two different hex color values where red is dominant."""
        result1 = generate_hex("red")
        result2 = generate_hex("red")
        
        # Check they're different
        self.assertNotEqual(result1, result2, "Two calls should return different values")
        
        # Check both have red dominant
        for result in [result1, result2]:
            r = int(result[0:2], 16)
            g = int(result[2:4], 16)
            b = int(result[4:6], 16)
            self.assertGreater(r, g, f"Red should dominate green: {r} > {g}")
            self.assertGreater(r, b, f"Red should dominate blue: {r} > {b}")
    
    def test_6_green_random_and_dominant(self):
        """Test 6: Calling generate_hex("green") twice should return two different hex color values where green is dominant."""
        result1 = generate_hex("green")
        result2 = generate_hex("green")
        
        # Check they're different
        self.assertNotEqual(result1, result2, "Two calls should return different values")
        
        # Check both have green dominant
        for result in [result1, result2]:
            r = int(result[0:2], 16)
            g = int(result[2:4], 16)
            b = int(result[4:6], 16)
            self.assertGreater(g, r, f"Green should dominate red: {g} > {r}")
            self.assertGreater(g, b, f"Green should dominate blue: {g} > {b}")
    
    def test_7_blue_random_and_dominant(self):
        """Test 7: Calling generate_hex("blue") twice should return two different hex color values where blue is dominant."""
        result1 = generate_hex("blue")
        result2 = generate_hex("blue")
        
        # Check they're different
        self.assertNotEqual(result1, result2, "Two calls should return different values")
        
        # Check both have blue dominant
        for result in [result1, result2]:
            r = int(result[0:2], 16)
            g = int(result[2:4], 16)
            b = int(result[4:6], 16)
            self.assertGreater(b, r, f"Blue should dominate red: {b} > {r}")
            self.assertGreater(b, g, f"Blue should dominate green: {b} > {g}")

if __name__ == "__main__":
    unittest.main()

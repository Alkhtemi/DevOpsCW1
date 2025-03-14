import unittest
from Dec2Hex import decimal_to_hex  # Import the function to test

class TestDecimalToHex(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(decimal_to_hex(0), "0")

    def test_positive_numbers(self):
        self.assertEqual(decimal_to_hex(10), "A")
        self.assertEqual(decimal_to_hex(255), "FF")
        self.assertEqual(decimal_to_hex(4096), "1000")

    def test_large_number(self):
        self.assertEqual(decimal_to_hex(123456789), "75BCD15")

if __name__ == "__main__":
    unittest.main()

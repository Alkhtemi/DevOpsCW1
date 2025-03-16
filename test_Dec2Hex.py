import unittest
from Dec2Hex import decimal_to_hex

class TestDecimalToHex(unittest.TestCase):

    def test_valid_integer_input(self):
        self.assertEqual(decimal_to_hex(10), "A")
        self.assertEqual(decimal_to_hex(255), "FF")
        self.assertEqual(decimal_to_hex(4095), "FFF")  # Additional valid input

    def test_zero_input(self):
        self.assertEqual(decimal_to_hex(0), "0")

    def test_no_input_provided(self):
        with self.assertRaises(SystemExit):
            decimal_to_hex()

    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            decimal_to_hex("abc")

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            decimal_to_hex(-1)

    def test_large_input(self):
        self.assertEqual(decimal_to_hex(65535), "FFFF")  # Large number

if __name__ == "__main__":
    unittest.main()

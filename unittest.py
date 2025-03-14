import unittest
from Dec2Hex import decimal_to_hex  # Import the function from your script

class TestDecimalToHex(unittest.TestCase):
    """
    Unit tests for the decimal_to_hex function.
    """

    def test_zero(self):
        """Test conversion of zero."""
        self.assertEqual(decimal_to_hex(0), "0")

    def test_positive_numbers(self):
        """Test conversion of positive integers."""
        self.assertEqual(decimal_to_hex(10), "A")
        self.assertEqual(decimal_to_hex(255), "FF")
        self.assertEqual(decimal_to_hex(4096), "1000")

    def test_large_number(self):
        """Test conversion of a large number."""
        self.assertEqual(decimal_to_hex(123456789), "75BCD15")

if __name__ == "__main__":
    unittest.main()

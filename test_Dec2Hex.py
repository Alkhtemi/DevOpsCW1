import unittest
import subprocess

class TestDecimalToHex(unittest.TestCase):
    """
    This class contains unit tests for the Dec2Hex.py script.
    Each test case validates a specific behavior of the script.
    """

    def test_valid_input(self):
        """
        Test valid integer inputs to ensure correct hexadecimal conversion.
        """
        # Test input: 15 (expected output: "Hexadecimal representation is: F")
        result_15 = subprocess.run(
            ["python3", "Dec2Hex.py", "15"],  # Command to run the script with input "15"
            capture_output=True,             # Capture the output of the script
            text=True                        # Ensure the output is returned as a string
        )
        self.assertEqual(
            result_15.stdout.strip(),        # Strip whitespace from the output
            "Hexadecimal representation is: F"
        )

        # Test input: 255 (expected output: "Hexadecimal representation is: FF")
        result_255 = subprocess.run(
            ["python3", "Dec2Hex.py", "255"],
            capture_output=True,
            text=True
        )
        self.assertEqual(
            result_255.stdout.strip(),
            "Hexadecimal representation is: FF"
        )

    def test_zero_input(self):
        """
        Test input of zero to ensure correct handling of edge case.
        """
        result = subprocess.run(
            ["python3", "Dec2Hex.py", "0"],
            capture_output=True,
            text=True
        )
        self.assertIn(
            "Hexadecimal representation is: 0",  # Check if the expected output is in the result
            result.stdout
        )

    def test_no_input_provided(self):
        """
        Test the behavior when no input is provided to the script.
        """
        result = subprocess.run(
            ["python3", "Dec2Hex.py"],  # No input argument provided
            capture_output=True,
            text=True
        )
        self.assertIn(
            "Warning: No input provided. Please enter a number.",  # Check for the warning message
            result.stdout
        )

    def test_non_integer_input(self):
        """
        Test the behavior when a non-integer input (e.g., "abc") is provided.
        """
        result = subprocess.run(
            ["python3", "Dec2Hex.py", "abc"],  # Non-integer input
            capture_output=True,
            text=True
        )
        self.assertIn(
            "Error: Invalid input. Please enter an integer.",  # Check for the error message
            result.stdout
        )

    def test_negative_input(self):
        """
        Test the behavior when a negative integer input is provided.
        """
        result = subprocess.run(
            ["python3", "Dec2Hex.py", "-5"],  # Negative integer input
            capture_output=True,
            text=True
        )
        self.assertIn(
            "Error: Please enter a non-negative integer.",  # Check for the error message
            result.stdout
        )

if __name__ == "__main__":
    """
    Entry point for running the unit tests.
    """
    unittest.main()

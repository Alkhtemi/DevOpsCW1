import subprocess, sys

def run_program(args):
    """Utility to run Dec2Hex.py with given args and return CompletedProcess."""
    return subprocess.run([sys.executable, "Dec2Hex.py", *args],
                          capture_output=True, text=True)

def test_valid_conversion():
    """Test a normal decimal to hex conversion."""
    result = run_program(["15"])
    assert result.returncode == 0
    # The program prints the hex representation; ensure it's correct
    assert "Hexadecimal representation is: F" in result.stdout

def test_no_input():
    """Test running the program with no arguments should produce an error and non-zero exit."""
    result = run_program([])  # no arguments
    # Expect an error message and an exit code indicating failure
    assert result.returncode != 0, "Expected non-zero exit code for missing input"
    assert "No input provided" in result.stdout  or "Usage" in result.stdout

def test_invalid_input():
    """Test that a non-integer input is handled gracefully."""
    result = run_program(["ABC"])
    # The program should not crash; it should return code 0 (handled) but print an error message
    assert result.returncode == 0, "Invalid input should not cause a non-zero exit (gracefully handled)"
    assert "Please provide a valid integer." in result.stdout

import sys

def decimal_to_hex(decimal_value):
    """Convert decimal to hexadecimal using Python's built-in function."""
    return f"{decimal_value:X}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No input provided. Enter a non-negative integer.")
        sys.exit(1)  # Fail build on missing input

    try:
        decimal_value = int(sys.argv[1])
        if decimal_value < 0:
            print("Error: Enter a non-negative integer.")
            sys.exit(1)  # Fail build on negative input

        hex_result = decimal_to_hex(decimal_value)
        print(f"Hexadecimal representation: {hex_result}")

    except ValueError:
        print("Error: Invalid input. Enter a valid integer.")
        sys.exit(1)  # Fail build on invalid input

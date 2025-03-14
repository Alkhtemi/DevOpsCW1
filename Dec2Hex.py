import sys

def decimal_to_hex(decimal_value):
    """Convert a decimal number to its hexadecimal representation.
    
    Args:
        decimal_value (int): Non-negative integer to convert.
        
    Returns:
        str: Uppercase hexadecimal string (e.g., "1A3F").
    """
    return f"{decimal_value:X}"  # Built-in Python conversion for simplicity

if __name__ == "__main__":
    # Validate input presence
    if len(sys.argv) < 2:
        print("Error: No input provided. Please enter a non-negative integer.")
        sys.exit(1)  # Fail build on missing input

    try:
        # Parse and validate input
        decimal_value = int(sys.argv[1])
        if decimal_value < 0:
            print("Error: Negative values are not allowed.")
            sys.exit(1)  # Fail build on negative input

        # Convert and print result
        hex_result = decimal_to_hex(decimal_value)
        print(f"Hexadecimal representation: {hex_result}")

    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        sys.exit(1)  # Fail build on non-integer input

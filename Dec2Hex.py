import sys

def decimal_to_hex(decimal_value):
    """Convert a decimal integer to its hexadecimal representation (as a string)."""
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    num = decimal_value

    print(f"Converting the Decimal Value {num} to Hex...")
    if num == 0:
        # If the decimal value is 0, directly return "0"
        hexadecimal = "0"
    else:
        # Continue dividing by 16 and building the hex string
        while num != 0:
            rem = num % 16
            hexadecimal = hex_chars[rem] + hexadecimal
            num //= 16
    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal  # Return the hexadecimal string for testing purposes

if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) > 1:
        try:
            decimal_value = int(sys.argv[1])
            decimal_to_hex(decimal_value)
        except ValueError:
            # Handle non-integer inputs
            print("Please provide a valid integer.")
            # Exit with code 0 to indicate graceful handling (not a crash)
            sys.exit(0)
    else:
        # No argument provided: print error and exit with non-zero status
        print("Error: No input provided. Please provide a decimal number.")
        sys.exit(1)

import sys

def decimal_to_hex(decimal_value):
    """
    Converts a given decimal value to its hexadecimal representation.
    
    Args:
        decimal_value (int): The decimal number to convert.
    
    Returns:
        str: The hexadecimal representation of the input decimal number.
    """
    # Define the mapping for hexadecimal characters
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    num = decimal_value

    print(f"Converting the Decimal Value {num} to Hex...")

    # Handle the special case where the input is 0
    if num == 0:
        print("Hexadecimal representation is: 0")
        return "0"

    # Perform the conversion
    while num != 0:
        rem = num % 16  # Get the remainder when divided by 16
        hexadecimal = hex_chars[rem] + hexadecimal  # Prepend the corresponding hex character
        num //= 16  # Update num by integer division with 16

    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal


if __name__ == "__main__":
    # Check if exactly one argument is provided (excluding the script name)
    if len(sys.argv) != 2:
        print("Error: Please provide exactly one integer input.")
        sys.exit(1)

    try:
        # Attempt to parse the input as an integer
        decimal_value = int(sys.argv[1])
        decimal_to_hex(decimal_value)
    except ValueError:
        # Handle cases where the input is not a valid integer
        print("Error: Input must be a valid integer.")
        sys.exit(1)

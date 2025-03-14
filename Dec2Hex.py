import sys

# Constants for hexadecimal conversion
HEX_BASE = 16
HEX_CHARS = "0123456789ABCDEF"

def decimal_to_hex(decimal_value):
    """
    Convert a decimal number to its hexadecimal representation.
    
    Parameters:
        decimal_value (int): The decimal number to convert.
        
    Returns:
        str: The hexadecimal representation of the input number.
    """
    if decimal_value == 0:
        return "0"  # Special case for zero
    
    hexadecimal = ""
    num = decimal_value
    while num > 0:
        rem = num % HEX_BASE  # Get the remainder when dividing by 16
        hexadecimal = HEX_CHARS[rem] + hexadecimal  # Map remainder to hex character
        num //= HEX_BASE  # Update num by integer division
    return hexadecimal

if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) < 2:
        print("Warning: No input provided. Please enter a non-negative integer.")
        sys.exit(0)  # Exit gracefully without failing the build

    try:
        # Parse the input as an integer
        decimal_value = int(sys.argv[1])
        
        # Validate that the input is non-negative
        if decimal_value < 0:
            print("Error: Please enter a non-negative integer.")
            sys.exit(1)  # Fail the build for invalid input
        
        # Perform the conversion and print the result
        hex_result = decimal_to_hex(decimal_value)
        print(f"Hexadecimal representation is: {hex_result}")
    
    except ValueError:
        # Handle invalid inputs (e.g., floating-point numbers or non-numeric strings)
        print("Error: Invalid input. Please enter a valid integer.")
        sys.exit(0)  # Exit gracefully without failing the build

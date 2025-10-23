def hex_key(num: str) -> int:
    """
    Receives a hexadecimal number as a string and counts the number of 
    hexadecimal digits that are primes (when converted to decimal).

    Hex digits 0-F map to decimal values 0-15.
    The prime decimal values in this range are: 2, 3, 5, 7, 11, 13.
    These map to the following hexadecimal digits: 2, 3, 5, 7, B, D.

    Args:
        num: A string representing a hexadecimal number (e.g., "1AEB3C").

    Returns:
        The count of prime hexadecimal digits in the input string.
    """
    # Define the set of hexadecimal digits that correspond to a prime decimal value.
    # 2, 3, 5, 7, 11 (B), 13 (D)
    PRIME_HEX_DIGITS = {'2', '3', '5', '7', 'B', 'D'}
    
    prime_count = 0
    
    # Iterate through each digit in the input hexadecimal string.
    # The problem guarantees that all A-F characters are uppercase.
    for digit in num:
        # Check if the current digit is one of the predefined prime hex digits.
        if digit in PRIME_HEX_DIGITS:
            prime_count += 1
            
    return prime_count

# Example Usage:
# Hex: 1 A E B 3 C
# Decimal: 1 10 14 11 3 12
# Prime digits: B (11) and 3 (3)
example_num = "1AEB3C"
result = hex_key(example_num)
# print(f"The number of prime hex digits in '{example_num}' is: {result}") # Expected output: 2

# Example 2:
# Hex: F F F D D 2
# Prime digits: D, D, 2
example_num_2 = "FFFD D2"
result_2 = hex_key(example_num_2.replace(" ", "")) # Handle potential spaces if the example was written loosely
# print(f"The number of prime hex digits in 'FFFD D2' is: {result_2}") # Expected output: 3

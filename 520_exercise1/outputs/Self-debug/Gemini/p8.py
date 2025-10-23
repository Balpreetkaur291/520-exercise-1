def hex_key(num: str) -> int:
    """
    Receives a hexadecimal number as a string and counts the number of 
    hexadecimal digits that are primes (based on their decimal value).
    
    The hexadecimal digits corresponding to prime decimal values (2, 3, 5, 7, 11, 13)
    are: '2', '3', '5', '7', 'B', and 'D'.

    Args:
        num: A string representing a hexadecimal number. Assumed to use 
             uppercase for A-F, or be an empty string.

    Returns:
        The count of prime hexadecimal digits found in the input string.
    """
    # Define the set of prime hexadecimal digits for efficient O(1) lookup.
    # (2, 3, 5, 7, 11(B), 13(D) are the prime decimal values < 16)
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    
    prime_count = 0
    
    # Iterate through each character (digit) in the input string
    for digit in num:
        # Check if the current digit is one of the pre-defined prime hex digits
        if digit in prime_hex_digits:
            prime_count += 1
            
    return prime_count
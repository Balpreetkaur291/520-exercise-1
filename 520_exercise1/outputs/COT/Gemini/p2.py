def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    
    # Handle the case for N=0, where the sum of digits is 0, and the binary is "0".
    if N == 0:
        return "0"

    # Step 1: Calculate the sum of the decimal digits of N
    sum_of_digits = 0
    temp_N = N  # Use a temporary variable for the loop
    
    while temp_N > 0:
        digit = temp_N % 10
        sum_of_digits += digit
        temp_N //= 10 # Integer division to drop the last digit

    # Step 2: Convert the sum to its binary string representation.
    # bin() returns a string prefixed with "0b", so we slice from the third character.
    binary_sum = bin(sum_of_digits)[2:]
    
    return binary_sum

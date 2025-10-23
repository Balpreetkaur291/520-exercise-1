def solve(N: int) -> str:
   """
   Given a non-negative integer N (0 ≤ N ≤ 10000), return the binary string
   of the sum of its decimal digits.
   """
   # Sum the digits of N
   digit_sum = sum(int(ch) for ch in str(N))
   # Convert the sum to binary string without the '0b' prefix
   return bin(digit_sum)[2:]

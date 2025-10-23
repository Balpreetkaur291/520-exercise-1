def solve(N: int) -> int:
    """
    Given a positive integer N, return the total sum of its digits in binary.
    This is equivalent to finding the population count (popcount) or Hamming weight of N.

    Args:
        N: A positive integer.

    Returns:
        The count of '1's in the binary representation of N.
    """
    if N <= 0:
        # Per the problem, N is a positive integer.
        # Handle non-positive input gracefully by returning 0,
        # as 0 has a binary sum of 0.
        return 0

    count = 0
    # Brian Kernighan's Algorithm:
    # N & (N - 1) clears the least significant set bit (the rightmost '1').
    # The loop runs exactly once for every set bit in N.
    while N > 0:
        count += 1
        N &= (N - 1)
    
    return count
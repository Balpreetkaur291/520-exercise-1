def fib4(n: int) -> int:
    """
    Computes the n-th element of the Fib4 number sequence efficiently 
    using dynamic programming with O(1) space complexity.

    The sequence is defined as:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4.
    
    Args:
        n: The index of the Fib4 number to compute (n >= 0).
        
    Returns:
        The n-th Fib4 number.
    """

    # 1. Handle base cases for n < 4
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0
    
    # 2. Initialization for the iterative process (O(1) space)
    # We use four variables to track the last four computed values:
    # a = fib4(i-4)
    # b = fib4(i-3)
    # c = fib4(i-2)
    # d = fib4(i-1)
    
    # Initialize for i=4 (where the loop begins):
    # a (fib4(0))
    a = 0
    # b (fib4(1))
    b = 0
    # c (fib4(2))
    c = 2
    # d (fib4(3))
    d = 0
    
    # 3. Iteratively compute the sequence up to n
    for i in range(4, n + 1):
        # Calculate the next term (fib4(i))
        next_fib = a + b + c + d
        
        # Shift the values for the next iteration:
        # The oldest value (a) is discarded.
        # The values shift one position to the left.
        a = b
        b = c
        c = d
        # The newest value (next_fib) becomes the last term (d).
        d = next_fib
        
    # The variable 'd' holds the result for fib4(n) after the loop completes
    return d
def is_prime(k: int) -> bool:
    """
    Checks if a number k is prime using an optimized trial division method 
    up to the square root of k.
    
    Args:
        k: The integer to check for primality.
    
    Returns:
        True if k is prime, False otherwise.
    """
    if k <= 1:
        # 0 and 1 are not prime.
        return False
    if k <= 3:
        # 2 and 3 are prime.
        return True
    
    # Check for divisibility by 2 and 3
    if k % 2 == 0 or k % 3 == 0:
        return False
    
    # Check for divisibility by numbers of the form 6k ± 1 (optimised check)
    i = 5
    while i * i <= k:
        if k % i == 0 or k % (i + 2) == 0:
            return False
        i += 6
        
    return True

def prime_fib(n: int) -> int:
    """
    prime_fib returns the n-th number that is a Fibonacci number and is also prime.
    
    The Fibonacci sequence used starts F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3, ...
    
    Args:
        n: The index (1-based) of the prime Fibonacci number to find.
        
    Returns:
        The n-th number that is both Fibonacci and prime.
        
    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer (1-based index).")

    # The first few Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, 13, ...
    # F(0)=0, F(1)=1, F(2)=1 are not prime.
    # We start with a = F(1) and b = F(2) to generate F(3) = 2 on the first iteration.
    a, b = 1, 1  # a = F(k-2), b = F(k-1)
    
    count = 0
    
    # Iterate indefinitely until the n-th result is found.
    while True:
        # Calculate the next Fibonacci number: F(k)
        # Python handles arbitrary precision integers, necessary for large Fibonacci numbers.
        next_fib = a + b
        
        # Shift the sequence forward: a -> F(k-1), b -> F(k)
        a, b = b, next_fib
        
        # Check if the new Fibonacci number is prime
        if is_prime(next_fib):
            count += 1
            if count == n:
                return next_fib

# Example Usage:
# F(3)=2 (1st prime fib)
# F(4)=3 (2nd prime fib)
# F(5)=5 (3rd prime fib)
# F(7)=13 (4th prime fib)
# print(f"1st prime Fibonacci number: {prime_fib(1)}")
# print(f"4th prime Fibonacci number: {prime_fib(4)}")

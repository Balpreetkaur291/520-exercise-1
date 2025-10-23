def is_prime(k: int) -> bool:
    """Checks if a number k is a prime number."""
    # Numbers less than 2 are not prime.
    if k < 2:
        return False
    # 2 is the smallest and only even prime number.
    if k == 2:
        return True
    # Even numbers greater than 2 are not prime.
    if k % 2 == 0:
        return False
    
    # Check for divisibility by odd numbers up to sqrt(k)
    i = 3
    # We only need to check up to the square root of k.
    while i * i <= k:
        if k % i == 0:
            return False
        i += 2
        
    return True

def prime_fib(n: int) -> int:
    """
    prime_fib returns the n-th number that is a Fibonacci number and is also prime.
    """
    if n <= 0:
        # Based on the problem's nature (n-th number), n should be positive.
        raise ValueError("n must be a positive integer.")

    # F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3, F(5)=5, ...
    
    # Initialize the Fibonacci sequence from F(1) and F(2)
    # The first few Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    # The first few prime Fibonacci numbers: 2, 3, 5, 13, 89, ...
    
    # Initialize two consecutive Fibonacci numbers
    f_prev = 1  # Corresponds to F(i-1)
    f_curr = 1  # Corresponds to F(i)
    
    # Counter for prime Fibonacci numbers found
    count = 0
    
    # Start iterating to find the next Fibonacci number (which will be >= 2)
    # The loop will find F(i+1) = f_prev + f_curr
    while True:
        # Calculate the next Fibonacci number
        f_next = f_prev + f_curr
        
        # Check if the next Fibonacci number is prime
        if is_prime(f_next):
            count += 1
            
            # Check if we have found the n-th prime Fibonacci number
            if count == n:
                return f_next
        
        # Update the previous two numbers for the next iteration
        f_prev = f_curr
        f_curr = f_next
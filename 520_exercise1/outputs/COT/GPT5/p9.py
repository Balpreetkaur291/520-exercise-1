def prime_fib(n: int):
    """
    Return the n-th Fibonacci number that is also prime (1-indexed).
    Examples:
        prime_fib(1) -> 2
        prime_fib(2) -> 3
        prime_fib(3) -> 5
        prime_fib(4) -> 13
        prime_fib(5) -> 89
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        if x in (2, 3):
            return True
        if x % 2 == 0 or x % 3 == 0:
            return False
        # Check possible factors of form 6k ± 1 up to sqrt(x)
        f = 5
        while f * f <= x:
            if x % f == 0 or x % (f + 2) == 0:
                return False
            f += 6
        return True

    # Fibonacci generator: F1 = 1, F2 = 1, F3 = 2, ...
    a, b = 1, 1
    found = 0
    while True:
        # test 'a' (current Fibonacci)
        if is_prime(a):
            found += 1
            if found == n:
                return a
        a, b = b, a + b
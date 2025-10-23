def prime_fib(n: int):
    """
    Return the n-th Fibonacci number that is also prime (1-indexed).
    Sequence begins: 2, 3, 5, 13, 89, 233, 1597, 28657, 514229, ...
    """

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    def is_probable_prime(x: int) -> bool:
        """Miller–Rabin primality test (deterministic for 64-bit; strong for larger)."""
        if x < 2:
            return False
        # small primes shortcut
        small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        if x in small_primes:
            return True
        for p in small_primes:
            if x % p == 0:
                return False

        # write x-1 as d * 2^s with d odd
        d = x - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1

        # Deterministic bases for 64-bit integers; for larger, still strong probabilistic
        # Ref: research on minimal base sets for 2^64
        bases = (2, 3, 5, 7, 11, 13, 17)

        def check(a: int) -> bool:
            y = pow(a, d, x)
            if y == 1 or y == x - 1:
                return True
            for _ in range(s - 1):
                y = (y * y) % x
                if y == x - 1:
                    return True
            return False

        for a in bases:
            if a % x == 0:  # skip if base equals modulus
                continue
            if not check(a):
                return False
        return True

    # Generate Fibonacci numbers and count those that are prime
    a, b = 0, 1  # F0=0, F1=1
    count = 0
    while True:
        a, b = b, a + b  # advance: a is current Fibonacci
        # Only check a >= 2
        if a >= 2 and is_probable_prime(a):
            count += 1
            if count == n:
                return a

def fib4(n: int) -> int:
    """
    Computes the n-th element of the Fib4 number sequence iteratively (non-recursive)
    with O(1) space complexity.

    The sequence is defined as:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4.
    """
    # Input validation (n must be non-negative)
    if n < 0:
        raise ValueError("Input 'n' must be a non-negative integer.")

    # Handle base cases
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    # O(1) space optimization: We only need the previous four terms.
    # We initialize them corresponding to fib4(0), fib4(1), fib4(2), fib4(3)
    # The variables represent:
    # a: fib4(i-4)
    # b: fib4(i-3)
    # c: fib4(i-2)
    # d: fib4(i-1)
    a, b, c, d = 0, 0, 2, 0

    # Iteratively compute fib4(i) from i=4 up to n
    for _ in range(4, n + 1):
        # Calculate the next term (e = fib4(i))
        e = a + b + c + d

        # Shift the values for the next iteration:
        # (a, b, c, d) becomes (b, c, d, e)
        a = b
        b = c
        c = d
        d = e

    # After the loop finishes (when i == n), 'd' holds the value of fib4(n).
    return d

# --- Example Usage and Verification ---

test_cases = [0, 1, 2, 3, 4, 5, 6, 7, 8]
expected_results = [0, 0, 2, 0, 2, 4, 8, 14, 28]

print("--- Fib4 Sequence Test (fib4(n) vs Expected) ---")
for n, expected in zip(test_cases, expected_results):
    result = fib4(n)
    print(f"fib4({n:2}) = {result:2} (Expected: {expected:2})")

# Example for a larger number
n_large = 10
print(f"\nfib4({n_large}) = {fib4(n_large)}") # Expected: 28 + 14 + 8 + 4 = 54
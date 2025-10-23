from typing import Union

Number = Union[int, float]

def fib4(n: Number) -> int:
    """
    Compute the n-th number of the Fib4 sequence iteratively.

    Definition:
        fib4(0) = 0
        fib4(1) = 0
        fib4(2) = 2
        fib4(3) = 0
        fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4

    Notes:
    - Accepts integer-valued floats (e.g., 5.0 is treated as 5).
    - Raises ValueError for negative n and TypeError for non-integral n.

    Time:  O(n)
    Space: O(1)
    """
    # Normalize input (treat integer-valued floats as ints)
    if isinstance(n, float):
        if not n.is_integer():
            raise TypeError("n must be an integer or an integer-valued float.")
        n = int(n)
    elif not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    # Base cases
    if n in (0, 1):
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    # Rolling window for last 4 terms: f0=fib4(k-4), f1=fib4(k-3), f2=fib4(k-2), f3=fib4(k-1)
    f0, f1, f2, f3 = 0, 0, 2, 0
    for _ in range(4, n + 1):
        f4 = f3 + f2 + f1 + f0
        f0, f1, f2, f3 = f1, f2, f3, f4
    return f3






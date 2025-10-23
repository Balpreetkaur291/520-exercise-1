def fib4(n: int):
    """
    The Fib4 number sequence:
      fib4(0)=0, fib4(1)=0, fib4(2)=2, fib4(3)=0,
      fib4(n)=fib4(n-1)+fib4(n-2)+fib4(n-3)+fib4(n-4) for n>=4.
    Computes the n-th Fib4 number without recursion.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    a0, a1, a2, a3 = 0, 0, 2, 0  # fib4(0)..fib4(3)
    for _ in range(4, n + 1):
        a0, a1, a2, a3 = a1, a2, a3, (a0 + a1 + a2 + a3)
    return a3

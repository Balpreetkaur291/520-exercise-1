def solve(N):
    """
    Given a positive integer N, return the total sum of its digits in binary.
    Accepts either an int (>=0) or a string of digits. Returns a binary string.
    """
    # Normalize input: allow int or digit-string
    if isinstance(N, int):
        if N < 0:
            N = -N  # make robust even if negative sneaks in
        s = str(N)
    elif isinstance(N, str):
        if not N.isdigit():
            raise ValueError("N as a string must contain only digits.")
        s = N
    else:
        raise TypeError("N must be an int or a string of digits.")

    total = sum(ord(ch) - 48 for ch in s)  # slightly faster than int(ch)
    return format(total, "b")

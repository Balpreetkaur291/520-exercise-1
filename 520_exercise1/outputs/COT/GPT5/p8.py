def hex_key(num: str) -> int:
    """
    Count how many characters in the hex string `num` correspond to prime numbers:
    2, 3, 5, 7, 11 (B), 13 (D).
    """
    prime_hex = {"2", "3", "5", "7", "B", "D"}
    if not num:
        return 0
    # Input is guaranteed uppercase, but .upper() makes it robust.
    return sum(1 for ch in num.upper() if ch in prime_hex)

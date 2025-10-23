def hex_key(num: str) -> int:
    """Count how many hex digits in `num` are primes: 2,3,5,7,B,D.
    Tolerates accidental lowercase by normalizing to uppercase.
    """
    prime_hex_digits = {"2", "3", "5", "7", "B", "D"}
    num = num.upper()
    return sum(1 for ch in num if ch in prime_hex_digits)
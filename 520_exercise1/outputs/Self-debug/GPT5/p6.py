# --- Initial implementation ---

def prod_signs_v1(arr):
    """
    Return (sum of magnitudes) * (product of signs) for a non-empty list of integers.
    If arr is empty, return None.
    """
    if arr is None or len(arr) == 0:
        return None

    total_abs = sum(abs(x) for x in arr)

    sign_prod = 1
    for x in arr:
        if x > 0:
            s = 1
        elif x < 0:
            s = -1
        else:
            s = 0
        sign_prod *= s

    return total_abs * sign_prod


# --- Review notes ---
# 1) Correctness: prod_signs_v1 returns None for empty, multiplies sum(|x|) with product of signs; zeros force result to 0. Correct.
# 2) Efficiency: If any element is 0, result is 0; we can early-return without summing magnitudes.
# 3) Simplicity: Product of signs can be computed via parity of negatives instead of iterative multiplication.


# --- Corrected & optimized implementation (final) ---

def prod_signs(arr):
    """
    Return (sum of magnitudes) * (product of signs) for a non-empty list of integers.
    Product of signs: 1 for positive, -1 for negative, 0 if any element is 0.
    Return None for empty arr.
    """
    if not arr:
        return None

    # Early exit: any zero makes the product of signs zero -> overall result zero.
    if any(x == 0 for x in arr):
        return 0

    total_abs = sum(abs(x) for x in arr)
    neg_count = sum(1 for x in arr if x < 0)
    sign = -1 if (neg_count % 2) else 1
    return total_abs * sign


# --- Quick sanity checks ---
if __name__ == "__main__":
    assert prod_signs([]) is None
    assert prod_signs([0]) == 0
    assert prod_signs([1, 2, 3]) == (1 + 2 + 3) * 1   # 6
    assert prod_signs([-1, -2, -3]) == (1 + 2 + 3) * (-1)  # -6
    assert prod_signs([-1, 2, -3]) == (1 + 2 + 3) * 1  # 6 (two negatives)
    assert prod_signs([4, 0, -5]) == 0
    # Cross-check with initial version
    for arr in ([], [0], [1,2,3], [-1,2,-3], [-1,-2,-3], [4,0,-5]):
        if arr:
            assert prod_signs(arr) == prod_signs_v1(arr)

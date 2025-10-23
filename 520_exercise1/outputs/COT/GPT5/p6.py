from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    """
    Return sum of magnitudes of integers multiplied by the product of their signs.
    - Sign is 1 for positive, -1 for negative, 0 for zero.
    - Return None for empty list.
    """
    if not arr:
        return None
    
    # If any zero exists, product of signs is 0 -> result is 0
    if any(x == 0 for x in arr):
        return 0
    
    sum_magnitudes = sum(abs(x) for x in arr)
    
    sign_product = 1
    for x in arr:
        sign_product *= (1 if x > 0 else -1)  # no zeros here due to early check
    
    return sign_product * sum_magnitudes

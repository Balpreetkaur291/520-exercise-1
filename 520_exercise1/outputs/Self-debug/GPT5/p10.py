from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Return (sum, product) for the list of integers.
    By definition:
      - sum([])   == 0
      - product([]) == 1
    """
    total = 0
    prod = 1
    for x in numbers:
        total += x
        prod *= x
    return total, prod

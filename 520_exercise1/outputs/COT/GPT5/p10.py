from typing import List, Tuple
import math
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    total = sum(numbers)
    prod = math.prod(numbers)  
    return total, prod
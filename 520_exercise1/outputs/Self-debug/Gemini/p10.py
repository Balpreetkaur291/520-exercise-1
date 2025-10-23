from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    For a given list of integers, return a tuple consisting of a sum and a product 
    of all the integers in a list.
    
    Empty sum should be equal to 0 and empty product should be equal to 1.
    
    Args:
        numbers: A list of integers.
        
    Returns:
        A tuple (sum, product) where sum is the total sum and product is the total 
        product of all elements in the list.
    """
    
    # Initialize sum (s) to 0. This is the identity element for addition, 
    # ensuring an empty list returns a sum of 0.
    s = 0
    
    # Initialize product (p) to 1. This is the identity element for multiplication, 
    # ensuring an empty list returns a product of 1.
    p = 1
    
    for number in numbers:
        # Accumulate the sum
        s += number
        
        # Accumulate the product
        p *= number
        
    return (s, p)

# --- Example Usage ---

# Test Case 1: Standard list
print(f"List [1, 2, 3, 4]: {sum_product([1, 2, 3, 4])}")
# Expected: (10, 24)

# Test Case 2: Empty list (Boundary condition)
print(f"List []: {sum_product([])}")
# Expected: (0, 1) - correctly handled by initial s=0, p=1

# Test Case 3: List containing zero
print(f"List [5, 0, 8]: {sum_product([5, 0, 8])}")
# Expected: (13, 0)

# Test Case 4: List with negative numbers
print(f"List [2, -3, 5]: {sum_product([2, -3, 5])}")
# Expected: (4, -30)

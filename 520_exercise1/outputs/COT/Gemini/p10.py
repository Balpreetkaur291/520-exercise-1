from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product 
    of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    """
    
    # Initialize the sum to the additive identity (0)
    total_sum: int = 0
    
    # Initialize the product to the multiplicative identity (1)
    total_product: int = 1
    
    # Iterate through the list to calculate the sum and product
    for num in numbers:
        total_sum += num
        total_product *= num
        
    # Return the results as a tuple
    return (total_sum, total_product)

# Example Usage (optional, for verification)
# print(sum_product([1, 2, 3, 4]))  # Expected: (10, 24)
# print(sum_product([]))             # Expected: (0, 1)
# print(sum_product([-1, 0, 5]))     # Expected: (4, 0)
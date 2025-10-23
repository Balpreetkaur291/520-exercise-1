def prod_signs(arr):
    """
    Calculates the sum of magnitudes of integers multiplied by the
    product of all signs (1, -1, or 0) in the array.

    Args:
        arr (list[int]): An array of integers.

    Returns:
        int/float: The product of the total magnitude sum and the total sign product.
        None: If the input array is empty.
    """
    
    # 1. Handle the boundary condition for an empty array
    if not arr:
        return None

    # 2. Calculate Sum of Magnitudes (must iterate over the entire array)
    # We use a generator expression with sum() for clarity and efficiency.
    sum_magnitudes = sum(abs(x) for x in arr)

    # 3. Calculate Product of Signs
    product_signs = 1

    for x in arr:
        # If any number is 0, the total product of signs is 0.
        # We can stop early as the result is determined.
        if x == 0:
            product_signs = 0
            break
        
        # If the number is negative, flip the current sign product.
        # If the number is positive, the product_signs remains unchanged (multiplied by 1).
        elif x < 0:
            product_signs *= -1
    
    # 4. Return the final result
    return sum_magnitudes * product_signs

# Example Usage:
# print(prod_signs([1, 2, -3]))     # Sum Mag (6) * Prod Sign (-1) = -6
# print(prod_signs([1, 0, 3]))      # Sum Mag (4) * Prod Sign (0) = 0
# print(prod_signs([-1, -2, -3]))   # Sum Mag (6) * Prod Sign (-1) = -6
# print(prod_signs([]))             # Returns None

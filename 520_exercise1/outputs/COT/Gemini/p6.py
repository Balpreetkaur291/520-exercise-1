def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.
    """
    
    # 1. Handle the Edge Case: Empty Array
    if not arr:
        return None
        
    # Initialize variables
    sum_magnitudes = 0
    product_signs = 1
    
    # 2. and 3. Calculate Sum of Magnitudes and Product of Signs simultaneously
    for x in arr:
        # Calculate the sum of magnitudes (absolute values)
        sum_magnitudes += abs(x)
        
        # Calculate the product of signs
        if x == 0:
            # If any element is 0, the product of signs must be 0.
            product_signs = 0
            # We can break early because the final result will be 0 * sum_magnitudes, which is 0.
            break 
        elif x < 0:
            # Multiply by -1 for a negative number
            product_signs *= -1
            
        # If x > 0, the sign is 1, and multiplying product_signs by 1 doesn't change it, 
        # so we don't need an explicit 'elif x > 0' branch.

    # 4. Calculate the Final Result
    # Result = sum of magnitudes * product of signs
    return sum_magnitudes * product_signs
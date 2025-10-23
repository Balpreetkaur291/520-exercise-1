from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:    
    # 1. Sort the list. This step is O(N log N).
    # Sorting allows us to only check adjacent elements.
    sorted_numbers = sorted(numbers)
    
    # 2. Iterate through the sorted list and check adjacent differences. 
    # This step is O(N).
    # We stop at len(sorted_numbers) - 1 because we check i and i+1.
    for i in range(len(sorted_numbers) - 1):
        num1 = sorted_numbers[i]
        num2 = sorted_numbers[i+1]
        
        # Calculate the absolute difference between the adjacent pair
        difference = num2 - num1  # Since it's sorted, difference is non-negative
        
        # Check the condition: is the difference less than the threshold?
        if difference < threshold:
            # Found a close pair, so we can immediately return True
            return True
            
    # If the loop finishes without finding a close pair, return False
    return False

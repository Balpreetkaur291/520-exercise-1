from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
   """
   Check whether any two numbers are closer than `threshold`.
   Uses sorting to achieve O(n log n) time and O(1) extra space (ignoring sort).
   """
   if threshold <= 0 or len(numbers) < 2:
       return False


   nums = sorted(numbers)
   for i in range(len(nums) - 1):
       if nums[i + 1] - nums[i] < threshold:
           return True
   return False
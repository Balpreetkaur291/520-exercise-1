from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    if threshold < 0 or len(numbers) < 2:
        return False
    nums = sorted(numbers)
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] < threshold:
            return True
    return False

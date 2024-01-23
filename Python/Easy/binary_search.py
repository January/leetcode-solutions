from typing import List

def search(nums: List[int], target: int) -> int:
    try:
        return nums.index(target)
    except ValueError:
        return -1
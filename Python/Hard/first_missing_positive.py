from typing import List
from bisect import bisect_left

def firstMissingPositive(nums: List[int]) -> int:
    res = [ele for ele in range(1, max(nums)+2) if ele not in nums]
    return res[0]

print(firstMissingPositive([7,8,9,11,12]))
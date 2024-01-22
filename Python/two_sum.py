# Runtime: Embarrassing
# Memory: 18MB (51.32%)

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in nums:
        for j in nums:
            if nums.index(i) != nums.index(j) and i + j == target:
                return [nums.index(i), nums.index(j)]

def twoSumTwo(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for i in range(0, length, 1):
        for j in range(0, length, 1):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]

print(twoSumTwo([2,7,11,15], 9))
print(twoSumTwo([3,2,4], 6))
print(twoSumTwo([3,3], 6))
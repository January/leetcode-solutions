from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for i in range(0, length, 1):
        for j in range(i + 1, length, 1):
            if nums[i] + nums[j] == target:
                return [i, j]

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
from typing import List

def numIdenticalPairs(nums: List[int]) -> int:
    numPairs = 0
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if i < j:
                if nums[i] == nums[j]:
                    numPairs += 1
    return numPairs

print(numIdenticalPairs([1,2,3,1,1,3]))
from typing import List

def findErrorNums(nums: List[int]) -> List[int]:
    nums.sort()
    nums_seen = []
    dupe_num = None
    missing_num = None
    for i in range(0, len(nums)):
        if nums[i] == nums[i+1]:
            dupe_num = nums[i]
            break
    for i in range(0, len(nums)):
        curr_num = i + 1
        if curr_num is not nums[i]:
            if curr_num != nums[i] and curr_num != dupe_num and curr_num not in nums:
                missing_num = curr_num
        nums_seen.append(nums[i])
    return [dupe_num, missing_num]

print(findErrorNums([1,2,2,4]))
print(findErrorNums([1,1]))
print(findErrorNums([2,2]))
print(findErrorNums([3,2,3,4,6,5]))
print(findErrorNums([1,5,3,2,2,7,6,4,8,9]))
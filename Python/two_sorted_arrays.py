from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    for i in nums2:
        nums1.append(i)
    nums1.sort()
    if(len(nums1) % 2 != 0):
        return nums1[len(nums1)//2]
    else:
        num1 = nums1[int((len(nums1) / 2) - 1)]
        num2 = nums1[int((len(nums1) / 2))]
        return((num1 + num2) / 2)

print(findMedianSortedArrays([1,2], [3,4]))
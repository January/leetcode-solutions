from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for j in range(n):
        nums1[m+j] = nums2[j]
    nums1.sort()

merge([1,2,3,0,0,0], 3, [2,5,6], 3)
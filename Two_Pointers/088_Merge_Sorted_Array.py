"""
Problem : 088. Merge Sorted Array

Link : https://leetcode.com/problems/merge-sorted-array/

Pattern : Two Pointers

Difficulty : Easy

Approach :
Start merging from the end of both arrays.
Place the larger element at the last available position in nums1.

Time Complexity : O(m + n)
Space Complexity : O(1)

"""

def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m-1
    j = n-1
    k = len(nums1)-1
    while i >= 0 and j >= 0:
        if nums1[i]>nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
        
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
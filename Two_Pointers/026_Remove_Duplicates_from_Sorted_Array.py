"""
Problem : 026. Remove Duplicates from Sorted Array

Link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Pattern : Two Pointers

Difficulty : Easy

Approach :
Maintain two pointers.
One pointer scans the array while the other keeps track of the position to place the next unique element.

Time Complexity : O(n)
Space Complexity : O(1)

"""

def removeDuplicates(nums):
    i = 1
    for j in range(1 , len(nums)):
        if nums[j] != nums[i-1]:
            nums[i] = nums[j]
            i += 1
    return i
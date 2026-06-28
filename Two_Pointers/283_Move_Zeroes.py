"""
Problem : 283. Move Zeroes

Link : https://leetcode.com/problems/move-zeroes/

Pattern : Two Pointers

Difficulty : Easy

Approach :
Move all non-zero elements to the front while preserving their order.
Fill the remaining positions with zeros.

Time Complexity : O(n)
Space Complexity : O(1)

"""

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    if 0 in nums:
        for j in range(i , len(nums)):
            if nums[j] != 0:
                nums[i] , nums[j] = nums[j] , nums[i]
                i += 1
    return nums
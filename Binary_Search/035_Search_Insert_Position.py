"""
Problem : 035. Search Insert Position

Link : https://leetcode.com/problems/search-insert-position/

Pattern : Binary Search

Difficulty : Easy

Approach :
Use binary search to either locate the target or determine the position where it should be inserted.

Time Complexity : O(log n)
Space Complexity : O(1)

"""

def searchInsert(nums,target):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] < target:
            low = mid+1
        elif nums[mid] > target:
            high = mid-1
        else:
            return mid
    return low
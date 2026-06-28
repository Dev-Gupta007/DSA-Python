"""
Problem : 704. Binary Search

Link : https://leetcode.com/problems/binary-search/

Pattern : Binary Search

Difficulty : Easy

Approach :
Repeatedly divide the search space in half.
Discard the half that cannot contain the target.

Time Complexity : O(log n)
Space Complexity : O(1)

"""

def search(nums,target):
    low = 0
    high = len(nums)-1
    mid =(low+high)//2
    while low<=high:
        mid =(low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1
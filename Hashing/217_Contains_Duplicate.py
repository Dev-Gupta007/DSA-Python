"""
Problem : 217. Contains Duplicate

Link : https://leetcode.com/problems/contains-duplicate/

Pattern : Hashing

Difficulty : Easy

Approach :
Store elements in a set.
If an element already exists, a duplicate is found.

Time Complexity : O(n)
Space Complexity : O(n)

"""

def containsDuplicate(nums):
    seen = set(nums)
    if len(seen) == len(nums):
        return False
    else:
        return True    

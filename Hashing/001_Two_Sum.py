"""
Problem : 001. Two Sum

Link : https://leetcode.com/problems/two-sum/

Pattern : Hashing

Difficulty : Easy

Approach :
Store previously seen numbers in a dictionary with their indices.
For each element, check if its complement exists in the dictionary.

Time Complexity : O(n)
Space Complexity : O(n)

"""

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1 , len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
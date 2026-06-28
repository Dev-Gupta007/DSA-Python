"""
Problem : 1480. Running Sum of 1D Array

Link : https://leetcode.com/problems/running-sum-of-1d-array/

Pattern : Arrays

Difficulty : Easy

Approach :
Traverse the array once while maintaining a cumulative sum.

Time Complexity : O(n)
Space Complexity : O(1)

"""

def runningSum(nums):
        total = 0
        ans = []
        for i in nums:
            total+=i
            ans.append(total)
        return ans
            
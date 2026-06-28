"""
Problem : 744. Find Smallest Letter Greater Than Target

Link : https://leetcode.com/problems/find-smallest-letter-greater-than-target/

Pattern : Binary Search

Difficulty : Easy

Approach :
Use binary search to find the first character greater than the target.
If no such character exists, return the first character.

Time Complexity : O(log n)
Space Complexity : O(1)

"""

def nextGreatestLetter(letters,target):
    low, high = 0, len(letters)
    while low < high:
        mid = (low + high) // 2
        if letters[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return letters[low % len(letters)]
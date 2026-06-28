"""
Problem : 349. Intersection of Two Arrays

Link : https://leetcode.com/problems/intersection-of-two-arrays/

Pattern : Hashing

Difficulty : Easy

Approach :
Convert one array into a set for O(1) lookups.
Iterate through the unique elements of the other array and collect common elements.

Time Complexity : O(n + m)
Space Complexity : O(n + m)

"""

def intersection(nums1, nums2):
    l = []
    nums2_set = set(nums2)
    for i in set(nums1):
        if i in nums2_set:
            l.append(i)

    return l
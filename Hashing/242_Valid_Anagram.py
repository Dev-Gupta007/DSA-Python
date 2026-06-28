"""
Problem : 242. Valid Anagram

Link : https://leetcode.com/problems/valid-anagram/

Pattern : Hashing

Difficulty : Easy

Approach :
Count the frequency of each character in both strings.
Compare the frequency maps.

Time Complexity : O(n)
Space Complexity : O(n)

"""

def isAnagram(self, s: str, t: str) -> bool:
    s_list = list(s)
    t_list = list(t)

    if len(s_list) != len(t_list):
        return False

    for i in set(s_list):
        if s_list.count(i) != t_list.count(i):
            return False
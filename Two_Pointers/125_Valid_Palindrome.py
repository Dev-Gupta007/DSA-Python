"""
Problem : 125. Valid Palindrome

Link : https://leetcode.com/problems/valid-palindrome/

Pattern : Two Pointers

Difficulty : Easy

Approach :
Use two pointers from both ends.
Skip non-alphanumeric characters and compare the remaining characters.

Time Complexity : O(n)
Space Complexity : O(1)

"""

def isPalindrome(s):
    test_str = ""
    for i in s:
        if i.isalnum():
            test_str += i.lower()
    if test_str == test_str[::-1]:
        return True
    else:
        return False
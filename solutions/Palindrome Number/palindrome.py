# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

class Solution(object):
    def isPalindrome(self, x):
        y = str(x)
        z = y[::1]
        if z == y:
            return True
        else:
            return False    
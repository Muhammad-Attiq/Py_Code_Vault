class Solution(object):
    def isPalindrome(self, x):
        rev = str(x)[::-1]
        y = str(x)
        if rev == y:
            return True
        else:
            return False

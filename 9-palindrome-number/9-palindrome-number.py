class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev, remainder = 0, 0
        temp = x
        while x > 0:
            remainder = x % 10
            rev = rev * 10 + remainder
            x = x // 10
        if temp == rev:
            return True
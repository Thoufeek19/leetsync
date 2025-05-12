class Solution:
    def isPalindrome(self, x: int) -> bool:
        z=str(x)
        s=z[::-1]
        if z==s:
            return True
        else:
            return False
        
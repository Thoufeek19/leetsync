class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            rev=i[::-1]
            if i==rev:
                return i
    
        return ""
        
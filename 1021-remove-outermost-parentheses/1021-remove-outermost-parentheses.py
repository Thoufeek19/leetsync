class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        t=list(s)
        t.pop()
        t.pop(0)        
        return str(s)
        
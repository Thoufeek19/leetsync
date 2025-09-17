class Solution:
    def repeatedCharacter(self, s: str) -> str:
        res=set()
        for i in s:
            if i not in res:
                res.add(i)
            else:
                return i


         
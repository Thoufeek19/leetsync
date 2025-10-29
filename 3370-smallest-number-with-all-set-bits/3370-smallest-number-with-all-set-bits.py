class Solution:
    def smallestNumber(self, n: int) -> int:
        res=bin(n)[2:]
        l=len(res)
        ans='1'*l
        return int(ans,2)
        
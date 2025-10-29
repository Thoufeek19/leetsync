class Solution:
    def removeZeros(self, n: int) -> int:
        res=str(n)
        ans=''
        for i in res:
            if i!='0':
                ans+=i
        return int(ans)

        
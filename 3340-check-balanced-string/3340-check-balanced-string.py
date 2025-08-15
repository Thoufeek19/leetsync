class Solution:
    def isBalanced(self, num: str) -> bool:
        even=0
        odd=0
        res=[]
        for i in num:
            value=int(i)
            res.append(value)
        for j in range(len(res)):
            if j%2==0:
                even+=res[j]
            else:
                odd+=res[j]
        if odd==even:
            return True
        else:
            return False
                
        
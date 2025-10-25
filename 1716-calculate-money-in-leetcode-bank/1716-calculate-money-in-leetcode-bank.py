import math
class Solution:
    def totalMoney(self, n: int) -> int:
        x=n//7
        s=n-(7*x)
        count=0
        for i in range(1,x+1):
            for j in range(i,i+7):
                count+=j
            
        for i in range(x+1,s+x+1):
             count+=i
        return count
        
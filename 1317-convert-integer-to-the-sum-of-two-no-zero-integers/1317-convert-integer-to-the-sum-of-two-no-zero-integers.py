import random
class Solution:

    def getNoZeroIntegers(self, n: int) -> List[int]:
        res=[]
        if n==2:
            res=[1,1]
            return res
        else:

            num = random.randint(1, n)  
            rem=n-num
            if num>rem:
                num,rem=rem,num
            res.append(num)
            res.append(rem)
            return res
        
            
         
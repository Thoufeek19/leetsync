class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in t:
            if j in d and d[j]>0:
                d[j]-=1
            else:
                return j
        
    
        
                

        
        
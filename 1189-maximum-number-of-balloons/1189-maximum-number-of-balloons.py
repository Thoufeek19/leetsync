import math
class Solution: 
    def maxNumberOfBalloons(self, text: str) -> int:

        d={'b':0,'a':0,'l':0,'o':0,'n':0}
        word=text.lower()
        


        for i in word:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        count_b=d['b']
        count_a=d['a']
        count_l=d['l']//2
        count_o=d['o']//2
        count_n=d['n']
        return min(count_b,count_a,count_l,count_o,count_n)
    
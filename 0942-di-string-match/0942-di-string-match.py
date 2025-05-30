class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        final=[]
        first,last=0,len(s)
        for i in s:
            if i=='I':
                final.append(first)
                first+=1
            else:
                final.append(last)
                last-=1
        final.append(first)
        return final
        
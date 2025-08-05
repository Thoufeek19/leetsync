class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        sam=['+','C','D']
        for i in range(len(operations)):
            if operations[i] not in sam:
                res.append(operations[i])
            elif operations[i]=='+':
                plus=int(res[-1])+int(res[-2])
                res.append(str(plus))
            elif operations[i]=='D':
                mul=int(res[-1])*2
                res.append(str(mul))
            elif operations[i]=='C':
                res.pop()
        count=0
        for i in res:
            count+=int(i)
        return count


        
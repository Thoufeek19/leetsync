class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans=[]
        res=[]
        for i in grid:
            for j in i:
                if j not in res:
                    res.append(j)
                else:
                    ans.append(j)
        base=[]
        for i in range(1,len(res)+2):
            base.append(i)
        for i in base:
            if i not in res:
                ans.append(i)
        return ans


        
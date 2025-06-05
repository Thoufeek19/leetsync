class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sums=0
        maxy=0
        d=[]
        for i in accounts:
            d.append(sum(i))
        return(max(d))
            
        
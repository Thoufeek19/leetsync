class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res=[]
        for i in range(len(prices)):
            dis=0
            for j in range(i+1,len(prices)):
                if j>i and prices[j]<=prices[i]:
                    dis=prices[j]
                    break
            res.append(prices[i]-dis)
                
                    
        return res
        
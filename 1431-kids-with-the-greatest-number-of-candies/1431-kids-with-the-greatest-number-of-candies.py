class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out=[]
        maxi=max(candies)
        for i in candies:
            if i+extraCandies>=maxi:
                out.append(True)
            else:
                out.append(False)
        return out
        
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        res=sorted(nums)
        a=res[-1]*res[-2]
        z=res[0]*res[1]
        return(a-z)
        
        
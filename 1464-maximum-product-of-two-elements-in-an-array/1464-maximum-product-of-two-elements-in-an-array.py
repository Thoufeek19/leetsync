class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=[]
        
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                d=(nums[i]-1)*(nums[j]-1)
                res.append(d)
               
        return max(res)
        
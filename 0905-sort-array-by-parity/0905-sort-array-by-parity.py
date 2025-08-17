class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res=[]
        ans=[]
        for i in nums:
            if i%2==0:
                res.append(i)
            else:
                ans.append(i)
        return res+ans
            
        
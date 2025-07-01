class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res=[]
        while nums:
            al=min(nums)
            nums.remove(al)
            bl=min(nums)
            nums.remove(bl)
            res.append(bl)
            res.append(al)
        return res
        
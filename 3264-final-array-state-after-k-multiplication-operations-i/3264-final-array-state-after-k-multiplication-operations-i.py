class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            miny=min(nums)
            res=miny*multiplier
            d=nums.index(miny)
            nums[d]=res
        return nums

            
        return nums        
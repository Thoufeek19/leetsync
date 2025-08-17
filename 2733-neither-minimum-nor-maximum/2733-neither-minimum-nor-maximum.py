class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)>2:

            res=sorted(nums)
            return res[1]
        else:
            return -1


        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = maxEnd = nums[0]
        for i in range(1, len(nums)):
            maxEnd = max(maxEnd + nums[i], nums[i])
            res = max(res, maxEnd)
        return res
        
class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        sums=0
        z=len(nums)
        for i in range(z):
            if i-k>=0 and nums[i]<=nums[i-k]:
                continue
            if i+k<z and nums[i]<=nums[i+k]:
                continue
            sums=sums+nums[i]
        return sums
        
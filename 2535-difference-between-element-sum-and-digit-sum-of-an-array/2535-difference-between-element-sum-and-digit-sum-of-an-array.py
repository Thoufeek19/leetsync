import math
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        maxy=0
        sums=sum(nums)
        for i in nums:
            if i<=9:
                maxy+=i
            else:
                for j in str(i):
                    maxy+=int(j)
        return abs(maxy-sums)

        
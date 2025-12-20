import math
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=[0]
        rightsum=[0]
        res=[]
        rev=nums[::-1]
        final=rightsum[::-1]
        for i in range(len(nums)):
            maxy=0
            if i+1<len(nums):
                maxy=leftsum[i]+nums[i]
                leftsum.append(maxy)
        for j in range(len(rev)):
            maxy=0
            if j+1<len(rev):
                maxy=rightsum[j]+rev[j]
                rightsum.append(maxy)
        final=rightsum[::-1]
        if len(nums)==1:
            return [0]
        else:

            for i in range(len(leftsum)):
                maxy=0
                maxy=abs(leftsum[i]-final[i])
                res.append(maxy)
            return res





        
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=0
        s=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]>nums[j] and i!=j:
                    count+=1
            s.append(count)
        return s
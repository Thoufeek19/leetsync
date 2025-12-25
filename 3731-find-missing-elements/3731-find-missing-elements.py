class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        arr=[]
        maxy=max(nums)
        miny=min(nums)
        # if nums[0]>nums[-1]:
        for i in range(miny,maxy+1):
            if i not in nums:
                arr.append(i)
        # else:

        #     for i in range(nums[0],nums[-1]+1):
        #         if i not in nums:
        #             arr.append(i)
        
        return sorted(arr)

        
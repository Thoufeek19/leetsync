class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg=[]
        for i in range(len(nums)//2):
            maxy=max(nums)
            miny=min(nums)
            average=(maxy+miny)/2
            nums.remove(maxy)
            nums.remove(miny)
            avg.append(average)
        return min(avg)
        
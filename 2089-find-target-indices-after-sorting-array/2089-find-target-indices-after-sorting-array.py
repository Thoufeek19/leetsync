class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res=[]
        sam=sorted(nums)
        for i in range(len(sam)):
            if sam[i]==target:
                res.append(i)
        return res

        
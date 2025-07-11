class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            for dig in str(i):
                res.append(int(dig))
        return res
        


        
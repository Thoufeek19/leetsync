class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s=set()
        res=[]
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                res.append(i)
        return res
        
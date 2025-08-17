class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        a=set(nums1)
        b=set(nums2)
        for i in a:
            for j in b:
                if i==j:
                    res.append(i)
        return res        
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res=[]
        ans=[]
        for i in nums1 :
            if i in nums2:
                res.append(i)
            elif i in nums3:
                res.append(i)
        for j in nums2:
            if j in nums1:
                res.append(j)
            elif j in nums3:
                res.append(j)
        for k in res:
            if k not in ans:
                ans.append(k)
        return ans
            

        
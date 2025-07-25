class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count=0
        maxy=0
        res=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                count+=1
        res.append(count)
        for j in range(len(nums2)):
            if nums2[j] in nums1:
                maxy+=1
        res.append(maxy)
        return res


        

        


        
        
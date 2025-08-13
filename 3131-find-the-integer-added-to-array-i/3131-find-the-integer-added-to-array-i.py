class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # ans=[]
        # for i in range(len(nums1)):
        #     for j in range(i,len(nums1)):
        #         dif=nums2[i]-nums1[j]
        #         ans.append(dif)
        # most_occured = max(set(ans), key=ans.count)
        # return most_occured
        nums1.sort()
        nums2.sort()
        return nums2[0]-nums1[0]
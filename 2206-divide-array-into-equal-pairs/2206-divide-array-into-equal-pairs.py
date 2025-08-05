from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        even=0
        odd=0
        count=Counter(nums)
        for i in count:
            if count[i]%2==0:
                even+=1
            else:
                odd+=1
        if odd==0:
            return True
        else:
            return False

        
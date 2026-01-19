class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        for i in range(0,len(nums)-1):
                j=i+1
                a=nums[0:i+1]
                b=nums[j:len(nums)+1]
                c=sum(a)-sum(b)
                print(a)
                print(b)
                print(c)
                if abs(c)%2==0:
                    count+=1
        return count
        
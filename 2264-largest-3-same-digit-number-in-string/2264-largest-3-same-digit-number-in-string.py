class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=[]

        for i in range(len(num)):
            if i+2<len(num):
                if num[i]==num[i+1]==num[i+2]:

                    a=""
                    a+=num[i]
                    a+=num[i+1]
                    a+=num[i+2]
                    ans.append(a)
        if len(ans)==0:
            return ""
        else:
            return max(ans)




            
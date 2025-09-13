class Solution:
    def finalString(self, s: str) -> str:
        # count=0
        # ans=list(s)
        # last=""
        # for k in ans:
        #     if k=='i':
        #         count+=1
        # for i in range(len(s)):
        #     if ans[i]=='i':
        #         b=s[0:i]
        #         res=b[::-1]+s[i+1:len(s)]
        # for j in s:
        #     if j!='i':
        #         last+=j
                       

        # if count%2==0:
        #     return last
        # else:
        #     return res
        ans=""
        for i in s:
            if i=='i':
                ans=ans[::-1]
            else:
                ans+=i
        return ans

        
        

        

        

        
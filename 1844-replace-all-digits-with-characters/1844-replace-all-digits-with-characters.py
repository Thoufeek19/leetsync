class Solution:
    def replaceDigits(self, s: str) -> str:
        ch=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        ans=""
        for i in range(len(s)):
            if s[i] not in ch:
                val=0
                tot=0
                val=ord(s[i-1])
                tot=val+int(s[i])
                ans+=(chr(tot))
            else:
                ans+=s[i]
        return ans


        
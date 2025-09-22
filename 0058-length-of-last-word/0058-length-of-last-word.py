class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count,z=0,len(s)-1
        while s[z]==" ":
            z-=1
        while z>=0 and s[z]!=" ":
            count+=1
            z-=1
        return count

            
        return count

            

        
class Solution:
    def maxFreqSum(self, s: str) -> int:
        maxv=0
        maxc=0
        vowels={'a','e','i','o','u'}
        fre={i:s.count(i) for i in set(s)}

        for j,count in fre.items():
            if j in vowels:
                maxv=max(maxv,count)
            else:
                maxc=max(maxc,count)
        return maxv+maxc
            
                
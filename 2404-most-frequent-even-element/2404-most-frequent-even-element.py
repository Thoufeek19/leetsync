class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d={}
        ans = -1
        max_count = 0
        for i in nums:
            # even & new
            if i % 2 == 0:
                if i not in d:
                    d[i] = 1
                    if d[i] > max_count:
                        ans = i
                        max_count = d[i]
                else:
                    d[i] += 1
                    if d[i] > max_count:
                        ans = i
                        max_count = d[i]
                    elif d[i] == max_count:
                        ans = min(ans, i)
        
        return ans
                
            
        
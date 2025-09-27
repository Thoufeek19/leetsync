class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # d={}
        # ans = -1 # elements (key)
        # max_count = 0 # max count (value)
        
        # for i in nums:
        #     # even & new
        #     if i % 2 == 0:
        #         if i not in d:
        #             d[i] = 1
        #             if d[i] > max_count:
        #                 ans = i
        #                 max_count = d[i]
        #             elif d[i] == max_count:
        #                 ans = min(ans, i)
        #         else:
        #             d[i] += 1
        #             if d[i] > max_count:
        #                 ans = i
        #                 max_count = d[i]
        #             elif d[i] == max_count:
        #                 ans = min(ans, i)
        
        # return ans
                
        # 2nd approach
        d = {}
        ans = -1
        for i in nums:
            if i % 2 != 0:
                continue
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        arr = []
        if len(d) > 0:
            max_value = max(d.values())
        else:
            return ans
        for i in d:
            if d[i] == max_value:
                arr.append(i)
        
        if len(arr) > 0:
            ans = min(arr)
        return ans
        
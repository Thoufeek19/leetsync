class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = float("-inf")
        for i in range(len(number)):
            if number[i] == digit:
                new = int(number[:i] + number[i+1:])
                ans = max(ans, new)
        
        return str(ans)
        
        1231, 1
        i = 0, 1
        new = number[:i] + number[i+1:] => 231
        i = 3, 1
        new = number[:i] => 123
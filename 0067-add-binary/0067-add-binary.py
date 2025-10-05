class Solution:
    def addBinary(self, a: str, b: str) -> str:
        val1 = int(a, 2)
        val2 = int(b, 2)
        ans = val1 + val2
        print(bin(ans))
        return bin(ans)[2:]
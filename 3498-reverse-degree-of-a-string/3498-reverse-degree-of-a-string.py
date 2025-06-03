class Solution:
    def reverseDegree(self, s: str) -> int:
        total=0
        for i,c in enumerate(s):
            postion=i+1
            reversed_value=ord('z')-ord(c)+1
            total+=postion*reversed_value
        return total
        
        
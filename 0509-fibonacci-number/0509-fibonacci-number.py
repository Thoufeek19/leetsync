class Solution:
    def fib(self, n: int) -> int:
            count=0
            a,b=0,1
            for i in range(n):
                count+=a
                a,b=b,a+b
            return a
            
        
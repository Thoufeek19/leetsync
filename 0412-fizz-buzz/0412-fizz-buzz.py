class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                s="FizzBuzz"
            elif i%5==0:
                 s="Buzz"
            elif i%3==0:
                s= "Fizz"
            else:
                s= str(i)
            a.append(s)
        return a


        
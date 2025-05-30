class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        counta=0
        countb=0
        n=len(s)//2
        z=len(s)
        a=s[:n]
        b=s[n:z]
        for i in a:
            if i=='a'or i=='e'or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I'or i=='O' or i=='U':
                counta+=1
        for i in b:
            if i=='a'or i=='e'or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I'or i=='O' or i=='U':
                countb+=1
        if counta==countb:
            return True
        else:
            return False
        
        

        
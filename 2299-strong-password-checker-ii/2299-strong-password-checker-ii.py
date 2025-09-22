class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        low=False
        upp=False
        digit=False
        spl=False
        adj=True
        if len(password) < 8:
            return False
        
        for i in range(0,len(password)):
            if password[i].islower():
                low = True
            if password[i].isupper():
                upp = True
            if password[i].isdigit():
                digit = True
            if i > 0 and password[i]==password[i-1]:
                adj = False
            if password[i] in "!@#$%^&*()-+":
                spl = True

        return low and upp and spl and adj and digit
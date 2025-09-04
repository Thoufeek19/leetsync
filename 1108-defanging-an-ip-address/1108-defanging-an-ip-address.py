class Solution:
    def defangIPaddr(self, address: str) -> str:
        z=list(address)
        s=[]
        for i in address:
            if i==".":
                s.append('[.]')
            else:
                s.append(i)
        return "".join(s)
        
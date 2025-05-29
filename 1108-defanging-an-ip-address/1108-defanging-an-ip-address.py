class Solution:
    def defangIPaddr(self, address: str) -> str:
        l=''
        for i in address:
            if i=='.':
                l+='[.]'
            else:
                l+=i
        return l
        
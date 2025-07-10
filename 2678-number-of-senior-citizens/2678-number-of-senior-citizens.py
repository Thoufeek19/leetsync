class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for i in details:
            s=''
            for c in i:
                if c.isdigit():
                    s+=c
            if int(s[10:12])>60:
                count+=1
        return count

        
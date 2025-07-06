class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res=list(s)
        count=0
        if len(words)==len(res):
            for i in range(len(words)):
                if words[i][0]==res[i]:
                    count+=1
        
        if count==len(words):
            return True
        else:
            return False

        
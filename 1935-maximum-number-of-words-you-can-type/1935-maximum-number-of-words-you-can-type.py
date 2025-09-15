class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count=0
        words=text.split()
        broken = set(brokenLetters)
    

        for word in words:
            if not (set(word) & broken): 
                count+=1
        return count



        
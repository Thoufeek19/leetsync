class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res=set()
        for i in range(len(words)):
            for j in words[i]:
                if j==x:
                    res.add(i)
        return list(res)


        
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        for i in words:
            if i[:len(pref)]==pref:
                count+=1
        return count

        
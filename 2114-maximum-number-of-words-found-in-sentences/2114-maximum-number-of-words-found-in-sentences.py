class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        word_count=0
        for i in sentences:
            wordy=i.split()
            maxy=len(wordy)
            word_count=max(maxy,word_count)
        return word_count

        
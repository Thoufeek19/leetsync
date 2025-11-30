class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split()
        arr=[1]*len(words)
        for i in words:
            num=int(i[-1])
            arr[num-1]=i[:-1]
        return " ".join(arr)
          
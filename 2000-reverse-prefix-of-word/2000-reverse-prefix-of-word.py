class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        arr=[]
        rem=[]
        for i in word:
            if i==ch:
                arr.append(i)
                break
            else:
                arr.append(i)
        for i in range(len(arr),len(word)):
            rem.append(word[i])
        if ch in word:
            final=arr[::-1]+rem
        else:
            final=arr
        return "".join(final)
        



        
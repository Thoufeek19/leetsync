class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        Reversed=[]
        fliped=[]
        for row in image:
            rev=row[::-1]
            Reversed.append(rev)
        for i in Reversed:
            fliping=[]
            for j in i:

                fliping.append(1-j)
            fliped.append(fliping)
        return fliped

        
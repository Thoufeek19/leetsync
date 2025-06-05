class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res=[]
        for i in range(len(names)):
            max_height=max(heights)
            index=heights.index(max_height)
            res.append(names[index])
            heights.pop(index)
            names.pop(index)
        return res


        
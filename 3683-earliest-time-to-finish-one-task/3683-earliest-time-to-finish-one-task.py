class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        count=0
        arr=[]
        for i in tasks:
            count=i[0]+i[1]
            arr.append(count)
        return min(arr)


        
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        s=set(friends)
        num=[]
        for i in order:
            if i in s:
                num.append(i)
        return num
        
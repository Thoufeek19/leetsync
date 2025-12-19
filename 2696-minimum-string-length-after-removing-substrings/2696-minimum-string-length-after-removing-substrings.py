class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        for i in s:
            if len(stack)>=1:
                if stack[-1]=="A" and i=="B":
                    stack.pop()
                elif stack[-1]=="C"and i=="D":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack)
        
class Solution:
    def maximum69Number (self, num: int) -> int:
        arr = [i for i in str(num)]  # list comprehension
        # print(arr)
        
        for i in range(len(arr)):
            if arr[i]=='6':
                arr[i]='9'
                break
        return int(''.join(arr))
            
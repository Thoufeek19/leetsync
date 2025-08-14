class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        bef=[]
        inb=[]
        aft=[]
        for i in nums:
            if i<pivot:
                bef.append(i)
            elif i==pivot:
                inb.append(i)
            elif i>pivot:
                aft.append(i)
        return bef+inb+aft
        
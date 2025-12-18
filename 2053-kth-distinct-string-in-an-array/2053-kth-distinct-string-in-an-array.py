class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        res=[]
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for key,value in d.items():
            if value==1:
                res.append(key)
        if k>len(res):
            return ""
        else:
            return res[k-1]
        
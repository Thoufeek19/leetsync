class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        z=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'
        ,'u','v','w','x','y','z']
        ans=[]
        count=0
        nope=0
        res=list(sentence)
        for i in res:
            if i in z:
                count+=1
                ans.append(i)
            else:
                nope+=1
        

        if nope>0:
            return False
        elif len(set(ans))==len(z):
            return True
        return False

        
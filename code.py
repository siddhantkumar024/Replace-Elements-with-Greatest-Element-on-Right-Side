class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        ans=[]
        n=len(arr)
        m=-1
        for i in range(n-1,-1,-1):
            c=arr[i]
            arr[i]=m
            m=max(c,m)
        return arr

            


        

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        arr=[True]*n
        res=0
        for i in range(2,n):
            if arr[i]:
                res+=1
                for j in range(i*i,n,i):
                    arr[j]=False
        return res

                
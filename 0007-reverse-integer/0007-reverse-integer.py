class Solution:
    def reverse(self, x: int) -> int:
        b=0
        if(x>=0):
            b=int(str(x)[::-1])
        else:
            b=int("-"+str(x)[:0:-1])

        if b<-2**31 or b>2**31:
            return 0
        return b
        
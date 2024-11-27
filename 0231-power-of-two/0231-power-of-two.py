class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        res=bin(n)[2:]
        if n>0 and res.count("1")==1:
            return True
        return False
        
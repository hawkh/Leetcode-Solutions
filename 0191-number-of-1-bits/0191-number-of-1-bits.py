class Solution:
    def hammingWeight(self, n: int) -> int:
        res=bin(n)[2:]
        return res.count("1")

        
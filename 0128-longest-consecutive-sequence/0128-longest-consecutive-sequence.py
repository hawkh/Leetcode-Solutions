class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ans=0
        longs=0
        for i in nums:
            if i-1  in s:
                continue
            l=0
            while i in s:
                i+=1
                l+=1
            longs=max(longs,l)
        return longs
        
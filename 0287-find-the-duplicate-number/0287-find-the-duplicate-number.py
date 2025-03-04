class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in nums:
            if d[i]:
                return i
            else:
                d[i]+=1
        
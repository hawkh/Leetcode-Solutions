class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1=temp=0
        for i in nums:
            if i==1:
                temp+=1
                max1=max(temp,max1)
            else:
                temp=0
        return max1
        
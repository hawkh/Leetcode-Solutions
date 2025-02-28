class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        currsum=0
        for num in nums:
            currsum=max(currsum+num,num)
            max_sum=max(currsum,max_sum)
        return max_sum
        
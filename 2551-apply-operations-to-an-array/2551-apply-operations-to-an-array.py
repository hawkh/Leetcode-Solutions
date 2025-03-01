class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        new=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0 
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            else:
                new.append(nums[i]) 
        for i in range(nums.count(0)):
            new.append(0)  
        return new
        
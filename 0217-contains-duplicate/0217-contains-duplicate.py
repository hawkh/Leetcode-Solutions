class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sortednums=sorted(nums)
        for i in range(len(nums)-1):
            curr=i
            nxt=i+1
            if sortednums[curr]==sortednums[nxt]:
                return True
        return False

        
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        wouldBeInserted = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                wouldBeInserted += 1
        return wouldBeInserted
        
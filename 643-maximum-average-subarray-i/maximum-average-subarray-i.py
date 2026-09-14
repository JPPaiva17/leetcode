class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum = sum(nums[0:k])
        maxSum = currentSum
        for i in range(1, len(nums) - k + 1):
            currentSum = currentSum - nums[i-1] + nums[i+k-1]
            maxSum = max(maxSum, currentSum)
        return maxSum / k
        
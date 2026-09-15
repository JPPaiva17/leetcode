class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        streak = 0
        countZero = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                countZero += 1
            while countZero > 1:
                if nums[left] == 0:
                    countZero -= 1
                left +=1
            streak = max(streak, right - left)
        return streak
            
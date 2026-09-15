class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxAmount = 0
        while(left < right):
            area = min(height[left], height[right]) * (right - left)
            maxAmount = max(maxAmount, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return maxAmount
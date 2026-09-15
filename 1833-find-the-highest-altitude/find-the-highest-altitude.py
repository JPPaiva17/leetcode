class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currentPoint = 0
        highestPoint = 0
        for i in range(len(gain)):
            currentPoint = currentPoint + gain[i]
            highestPoint = max(currentPoint, highestPoint)
        return highestPoint



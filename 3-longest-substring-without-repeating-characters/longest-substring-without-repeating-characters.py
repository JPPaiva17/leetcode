class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxCount = 0
        letterDict = {}

        for end, c in enumerate(s):
            if c in letterDict and letterDict[c] >= start:
                start = letterDict[c] + 1
            letterDict[c] = end
            maxCount = max(maxCount, end - start + 1)
        return maxCount
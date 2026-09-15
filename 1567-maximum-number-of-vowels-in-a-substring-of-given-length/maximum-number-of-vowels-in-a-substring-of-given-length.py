class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiouAEIOU")
        actualCount = sum(1 for c in s[:k] if c in vowels)
        nextCount = actualCount
        for i in range(1, len(s) - k + 1):
            if s[i - 1] in vowels:
                nextCount -=1
            if s[i + k - 1] in vowels:
                nextCount +=1
            actualCount = nextCount if nextCount > actualCount else actualCount
        return actualCount


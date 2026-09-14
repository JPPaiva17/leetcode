class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        countEqual = 0
        for c in t:
            if countEqual < len(s) and s[countEqual] == c:
                countEqual += 1
        return countEqual == len(s)
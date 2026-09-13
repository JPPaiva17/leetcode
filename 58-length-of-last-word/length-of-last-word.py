class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 1
        for i in range(1, len(s)):
            if s[i-1] == ' ' and s[i] != ' ':
                length = 1
            elif s[i] != ' ':
                length += 1

        return length
        
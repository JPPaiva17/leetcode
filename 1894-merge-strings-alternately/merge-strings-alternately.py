class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i = 0
        for i in range(min(len(word1), len(word2))):
            merged.append(word1[i])
            merged.append(word2[i])
        merged.append(word1[i+1:] if word1 else "")
        merged.append(word2[i+1:] if word1 else "")

        return "".join(merged)
            
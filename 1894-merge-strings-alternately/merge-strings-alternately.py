class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        AlternatelyWord = ""
        for i in range(min(len(word1), len(word2))):
            AlternatelyWord = AlternatelyWord + word1[i] + word2[i]
        
        AlternatelyWord = AlternatelyWord + word1[i+1:] + word2[i+1:]
        return AlternatelyWord
            
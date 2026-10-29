class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        finalWord = []
        minLen = min(len(word1), len(word2))
        for i in range(minLen):
            finalWord += word1[i] + word2[i]

        finalWord.append(word1[minLen:])
        finalWord.append(word2[minLen:])
    
        return "".join(finalWord)
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        mapW1 = {}
        mapW2 = {}

        if len(word1) != len(word2):
            return False

        for i in range(len(word1)):
            if word1[i] in mapW1:
                mapW1[word1[i]] += 1
            else:
                mapW1[word1[i]] = 1

            if word2[i] in mapW2:
                mapW2[word2[i]] += 1
            else:
                mapW2[word2[i]] = 1

        return set(mapW1) == set(mapW2) and sorted(mapW1.values()) == sorted(mapW2.values())
        
# 1. Same length
# 2. Same set of chars
# 3. Same set of frequency

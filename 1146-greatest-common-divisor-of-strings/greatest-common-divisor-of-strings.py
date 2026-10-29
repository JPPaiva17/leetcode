class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 == str2+str1:
            a = max(len(str1), len(str2))
            b = min(len(str1), len(str2))
            mdc = 0
            while b != 0:
                a, b = b, a%b
            return str1[:a]
        return "" 
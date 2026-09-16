class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hashMap = {}

        for n in nums:
            if n not in hashMap:
                hashMap[n] = 1
            else:
                hashMap[n] += 1
        
        for k, v in hashMap.items():
            if v == 1:
                return k 
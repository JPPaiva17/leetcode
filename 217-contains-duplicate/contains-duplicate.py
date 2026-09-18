class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numbers = {}
        for n in nums:
            if n in numbers:
                return True
            else:
                numbers[n] = 1
        return False
        
        
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        numsDictionary = {}
        for i in range(len(nums)):
            if nums[i] in numsDictionary:
                distance = i - numsDictionary[nums[i]]
                if distance <= k:
                    return True
                else:
                    numsDictionary[nums[i]] = i
            else:
                numsDictionary[nums[i]] = i
        return False
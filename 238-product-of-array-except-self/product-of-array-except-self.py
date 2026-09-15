class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        for i in range(1, len(nums)):
            answer[i] = nums[i - 1] * answer[i-1] 

        sufixo = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= sufixo
            sufixo *= nums[i]

        return answer
            
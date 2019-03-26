class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(list({num for num in nums if num > 0}))
        prev = 0
        for num in nums:
            if num - prev > 1:
                return prev + 1
            prev = num
        return prev + 1

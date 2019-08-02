class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        count = len(nums)
        if count == 0:
            return None
        elif count == 1:
            return 0
        for i in range(count - 1):
            if nums[i] > nums[i + 1]:
                return i
        return count - 1

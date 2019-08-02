class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        count = len(nums)
        
        if count < 2:
            return 0
        
        nums.sort()
        max_gap = nums[1] - nums[0]
        for i in range(1, count - 1):
            max_gap = max(max_gap, nums[i + 1] - nums[i])
            
        return max_gap

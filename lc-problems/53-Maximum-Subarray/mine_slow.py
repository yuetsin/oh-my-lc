class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        numcnt = len(nums)
        rst = None
        for i in range(numcnt):
            j = i
            sum_up = 0
            max_sum = None
            while j < numcnt:
                sum_up += nums[j]
                if max_sum == None or sum_up > max_sum:
                    max_sum = sum_up
                j += 1
            if rst == None or rst < max_sum:
                rst = max_sum
        return rst

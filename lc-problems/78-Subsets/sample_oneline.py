class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[num for j, num in enumerate(nums) if i & (1 << j)] for i in range(1 << len(nums))]

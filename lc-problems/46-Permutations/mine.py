class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numlen = len(nums)
        if numlen == 1:
            return [nums]
        elif numlen == 2:
            return [nums, [nums[1], nums[0]]]
        else:
            rst = []
            for i in range(numlen):
                nums[0], nums[i] = nums[i], nums[0]
                rst += [[nums[0]] + ls for ls in self.permute(nums[1:])]
                nums[0], nums[i] = nums[i], nums[0]
            return rst

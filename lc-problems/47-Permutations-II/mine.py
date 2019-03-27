class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        numlen = len(nums)
        if numlen == 1:
            return [nums]
        elif numlen == 2:
            if nums[0] == nums[1]:
                return [nums]
            else:
                return [nums, [nums[1], nums[0]]]
        else:
            rst = []
            for i in range(numlen):
                if i != 0 and nums[i] in nums[:i]:
                    continue
                nums[0], nums[i] = nums[i], nums[0]
                rst += [[nums[0]] + ls for ls in self.permuteUnique(nums[1:])]
                nums[0], nums[i] = nums[i], nums[0]
            return rst
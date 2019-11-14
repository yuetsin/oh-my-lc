#!/usr/bin/env python


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.counts = len(nums)
        self.idx = list(range(self.counts))

    def pick(self, target: int) -> int:
        random.shuffle(self.idx)
        for i in self.idx:
            if self.nums[i] == target:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

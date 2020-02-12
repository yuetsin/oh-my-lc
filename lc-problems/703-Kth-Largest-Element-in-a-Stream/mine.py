#!/usr/bin/env python

import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.nums.sort()
        self.k = k
        if len(nums) > k:
            # trim it
            self.nums = self.nums[-k:]

    def add(self, val: int) -> int:
        bisect.insort_left(self.nums, val)
        
        if len(self.nums) > self.k:
            self.nums.pop(0)
            
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
#!/usr/bin/env python


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Note:
        # Your algorithm should run in O(n) time complexity
        # and O(1) space complexity.
        # 有什么办法可以只遍历一次？
        # 还不准用额外空间？

        if not nums:
            return False

        top_first = max(nums) + 1
        second_first = top_first

        for num in nums:
            if num <= top_first:
                top_first = num
            elif num <= second_first:
                second_first = num
            else:
                return True

        return False

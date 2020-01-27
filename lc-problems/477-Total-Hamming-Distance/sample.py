#!/usr/bin/env python


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        nums_len = len(nums)

        if (nums_len == 0):
            return 0

        current_bit = 1
        ret = 0
        max_ = max(nums)

        while (current_bit <= max_):
            counter = 0

            for number in nums:
                if (number & current_bit):
                    counter += 1

            ret += counter * (nums_len - counter)
            current_bit <<= 1

        return ret

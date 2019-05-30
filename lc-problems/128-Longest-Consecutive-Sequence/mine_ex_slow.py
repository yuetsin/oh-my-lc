#!/usr/bin/env python3


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        minv = min(nums)
        maxv = max(nums)
        num_set = set(nums)

        # print(nums)
        # size = len(nums)

        # b = [False] * (size)

        max_cnt = 0
        cur_cnt = 0
        for i in range(minv, maxv + 1):
            if i in num_set:
                cur_cnt += 1
            else:
                if max_cnt < cur_cnt:
                    max_cnt = cur_cnt
                cur_cnt = 0
        if cur_cnt > max_cnt:
            max_cnt = cur_cnt

        return max_cnt

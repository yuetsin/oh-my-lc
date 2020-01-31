#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        num_cnt = len(nums)
        if num_cnt < 2:
            return False

        sums = [0]
        current_sum = 0

        for num in nums:
            current_sum += num
            sums.append(current_sum)

        # print(sums)
        for i in range(1, num_cnt):
            for j in range(i + 1, num_cnt + 1):
                # print("Detect between [%d:%d]" % (i, j))
                if k == 0:
                    if sums[j] - sums[i - 1] == 0:
                        return True
                else:
                    if (sums[j] - sums[i - 1]) % k == 0:
                        return True

        return False

#!/usr/bin/env python


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        if not nums:
            return -1

        presum = [0]

        current = 0

        for num in nums:
            current += num
            presum.append(current)

        # print(presum)

        total_sum = presum[-1]

        for i in range(len(nums)):
            if total_sum - presum[i + 1] == presum[i]:
                return i

        return -1

#!/usr/bin/env python


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = [0]
        cnt = 0
        for num in nums:
            cnt += num
            sums.append(cnt)

        max_avg = float('-inf')
        for i in range(len(sums) - k):
            max_avg = max(max_avg, (sums[i + k] - sums[i]) / k)

        return max_avg

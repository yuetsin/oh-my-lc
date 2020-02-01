#!/usr/bin/env python

import bisect


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def splitTime(string: str) -> int:
            hour, minute = string.split(':')
            return int(hour) * 60 + int(minute)

        times = []
        for time in timePoints:
            bisect.insort_left(times, splitTime(time))

        if len(times) > 1:
            times.append(times[0] + 1440)

        # print(times)

        min_diff = float('+inf')

        for i in range(len(times) - 1):
            min_diff = min(min_diff, times[i + 1] - times[i])
        return min_diff

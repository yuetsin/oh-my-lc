#!/usr/bin/env python


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #         hashable_intervals = []
        #         for interval in intervals:
        #             # assert(len(interval) == 2)
        #             hashable_intervals.append((interval[0], interval[1]))
        intervals.sort()  # sort start
        count = -1
        smallerEnd = float('inf')
        for a, b in intervals:
            if smallerEnd > a:  # overlap
                count += 1
                smallerEnd = min(smallerEnd, b)
            else:
                smallerEnd = b
        return max(0, count)

#!/usr/bin/env python


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def isRight(i: List[int], j: List[int]) -> bool:
            return j[0] >= i[1]
        for i in range(len(intervals)):
            intervals[i].append(i)

        intervals.sort()
        length = len(intervals)

        result = [-1] * length
        for i in range(length - 1):
            for j in range(i + 1, length):
                if intervals[i][1] <= intervals[j][0]:
                    result[intervals[i][2]] = intervals[j][2]
                    break

        return result

#!/usr/bin/env python


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) <= 0:
            return 0
        res = []
        points.sort(key=lambda x: x[1])
        res.append(points[0])
        for i in range(1, len(points)):
            if points[i][0] <= res[-1][1]:
                continue
            else:
                res.append(points[i])
        return len(res)

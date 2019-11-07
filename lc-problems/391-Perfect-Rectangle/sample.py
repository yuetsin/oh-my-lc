#!/usr/bin/env python

from typing import List
from collections import defaultdict


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        def mergeInterval(intervals):
            res = []
            intervals.sort()
            for interval in intervals:
                if not res or res[-1][1] < interval[0]:
                    res.append(interval)
                elif res[-1][1] == interval[0]:
                    res[-1][1] = interval[1]
                else:
                    return []
            return res

        rectangles.sort()
        bottom_line = rectangles[0][0]
        top_line = max(x[2] for x in rectangles)

        interval_dict = defaultdict(list)
        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle
            interval_dict[(x1, True)] += [[y1, y2]]
            interval_dict[(x2, False)] += [[y1, y2]]

        for key in interval_dict.keys():
            if not key[1]:
                continue
            counter_key = (key[0], False) if key[0] != bottom_line else (
                top_line, False)
            pos_edges = mergeInterval(interval_dict[key])
            neg_edges = mergeInterval(interval_dict[counter_key])
            if not pos_edges or not neg_edges or pos_edges != neg_edges:
                return False

        return True

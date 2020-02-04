#!/usr/bin/env python

from fractions import Fraction


class Solution:

    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:

        def slope(a, b):
            num, denom = b[1] - a[1], b[0] - a[0]
            return Fraction(num, denom) if denom else float("inf")

        def hull(pts, comp=operator.lt):
            hull = [pts[0]]
            for pt in pts[1:]:
                prev = hull.pop()
                while hull and comp(slope(hull[-1], prev), slope(prev, pt)):
                    prev = hull.pop()
                hull.extend([prev, pt])
            return hull

        points.sort()
        upper_hull = hull(points)
        lower_hull = hull(points, operator.gt)
        return set(map(tuple, lower_hull + upper_hull))

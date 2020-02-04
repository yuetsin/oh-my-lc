#!/usr/bin/env python


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(p1: List[int], p2: List[int]) -> bool:
            return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (p2[0] - p1[0])

        def check(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
            return dist(p1, p2) > 0 and dist(p1, p2) == dist(p2, p3) and dist(p2, p3) == dist(p3, p4) and dist(p3, p4) == dist(p4, p1) and dist(p1, p3) == dist(p2, p4)

        return check(p1, p2, p3, p4) or check(p1, p3, p2, p4) or check(p1, p2, p4, p3)

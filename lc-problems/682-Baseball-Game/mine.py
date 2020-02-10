#!/usr/bin/env python


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        points = []

        for op in ops:
            if op == '+':
                if len(points) >= 2:
                    points.append(points[-1] + points[-2])
            elif op == 'D':
                if len(points) >= 1:
                    points.append(points[-1] * 2)
            elif op == 'C':
                if len(points) >= 1:
                    points.pop(-1)
            else:
                points.append(int(op))

        return sum(points)

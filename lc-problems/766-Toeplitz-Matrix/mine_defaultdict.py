#!/usr/bin/env python

from collections import defaultdict


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        y_max = len(matrix)
        x_max = len(matrix[0])

        offsets = defaultdict(list)

        for x in range(x_max):
            for y in range(y_max):
                offsets[x - y].append(matrix[y][x])

        for _, v in offsets.items():
            if any([i != v[0] for i in v]):
                return False

        return True

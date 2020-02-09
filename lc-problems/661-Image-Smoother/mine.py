#!/usr/bin/env python

import numpy as np


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:

        max_y = len(M)
        if max_y == 0:
            return []

        max_x = len(M[0])

        result = [[0] * max_x for _ in range(max_y)]

        for x in range(max_x):
            for y in range(max_y):

                vals = []
                for i in range(max(x - 1, 0), min(x + 2, max_x)):
                    for j in range(max(y - 1, 0), min(y + 2, max_y)):
                        vals.append(M[j][i])

                result[y][x] = sum(vals) // len(vals)

        return result

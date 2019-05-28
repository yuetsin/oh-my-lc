#!/usr/bin/env python3


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        #
        # [
        # [2],
        # [3,4],
        # [6,5,7],
        # [4,1,8,3]
        # ]
        #

        max_depth = len(triangle)

        DP_table = []

        for i in range(max_depth):
            DP_table.append([-1] * (i + 1))

        def minPathSince(i, j) -> int:
            if i >= max_depth:
                return 0

            if DP_table[i][j] == -1:
                minVal = min(minPathSince(i + 1, j),
                             minPathSince(i + 1, j + 1))
                DP_table[i][j] = minVal + triangle[i][j]

            return DP_table[i][j]

        return minPathSince(0, 0)

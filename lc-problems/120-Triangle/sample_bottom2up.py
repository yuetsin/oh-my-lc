#!/usr/bin/env python


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        return self.bottomToUp(triangle)

    def bottomToUp(self, triangle):
        res = triangle[-1]
        for row in xrange(len(triangle) - 2, -1, -1):
            for col in xrange(row + 1):
                res[col] = min(res[col], res[col + 1]) + triangle[row][col]
        return res[0]

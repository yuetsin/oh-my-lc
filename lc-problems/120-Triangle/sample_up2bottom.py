#!/usr/bin/env python


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        return self.upToBottom(triangle)

    def upToBottom(self, triangle):
        if len(triangle) == 0:
            return 0
        n = len(triangle)
        res = [0] * n
        for row in xrange(n):
            for col in xrange(row, -1, -1):
                if col == 0:
                    res[0] += triangle[row][0]
                elif col == row:
                    res[row] = res[row - 1] + triangle[row][row]
                else:
                    res[col] = min(res[col - 1], res[col]) + triangle[row][col]
            print res
        return min(res)

#!/usr/bin/env python


def kthSmallest(self, matrix, k):
    ans = []
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return ans
    h = []
    row, col = min(len(matrix), k), min(len(matrix[0])-1, k)
    for i in xrange(row):
        heapq.heappush(h, [matrix[i][0], i, 0])
    s = k
    while s > 0 and h:
        ans, i, j = heapq.heappop(h)
        if j < col:
            heapq.heappush(h, [matrix[i][j+1], i, j+1])
        s -= 1
    return ans

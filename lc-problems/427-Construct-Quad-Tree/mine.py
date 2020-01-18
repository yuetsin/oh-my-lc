#!/usr/bin/env python

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def allTheSame(x: int, y: int, size: int) -> bool:

            head = grid[y][x]
            for ix in range(x, x + size):
                for iy in range(y, y + size):
                    if head != grid[iy][ix]:
                        return False

            return True

        def constructAt(x: int, y: int, size: int) -> 'Node':
            if allTheSame(x, y, size):
                return Node(grid[y][x], True, None, None, None, None)

            half = size // 2
            return Node(None, False, constructAt(x, y, half), constructAt(x + half, y, half),
                        constructAt(x, y + half, half), constructAt(x + half, y + half, half))

        return constructAt(0, 0, len(grid))

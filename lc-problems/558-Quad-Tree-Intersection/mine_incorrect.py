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
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf and quadTree2.isLeaf:
            return Node(quadTree1.val or quadTree2.val, True, None, None, None, None)

        if (not quadTree1.isLeaf) and (not quadTree2.isLeaf):
            return Node(None, False,
                        self.intersect(quadTree1.topLeft, quadTree2.topLeft),
                        self.intersect(quadTree1.topRight, quadTree2.topRight),
                        self.intersect(quadTree1.bottomLeft,
                                       quadTree2.bottomLeft),
                        self.intersect(quadTree1.bottomRight, quadTree2.bottomRight))

        if quadTree1.isLeaf:
            # 1 是 Leaf，2 不是
            if quadTree1.val:
                return quadTree1
            else:
                return Node(None, False,
                            self.intersect(
                                Node(quadTree1.val, True, None, None, None, None), quadTree2.topLeft),
                            self.intersect(
                                Node(quadTree1.val, True, None, None, None, None), quadTree2.topRight),
                            self.intersect(
                                Node(quadTree1.val, True, None, None, None, None), quadTree2.bottomLeft),
                            self.intersect(Node(quadTree1.val, True, None, None, None, None), quadTree2.bottomRight))

        if quadTree2.isLeaf:
            if quadTree2.val:
                return quadTree2
            else:
                return Node(None, False,
                            self.intersect(
                                Node(quadTree2.val, True, None, None, None, None), quadTree1.topLeft),
                            self.intersect(
                                Node(quadTree2.val, True, None, None, None, None), quadTree1.topRight),
                            self.intersect(
                                Node(quadTree2.val, True, None, None, None, None), quadTree1.bottomLeft),
                            self.intersect(Node(quadTree2.val, True, None, None, None, None), quadTree1.bottomRight))

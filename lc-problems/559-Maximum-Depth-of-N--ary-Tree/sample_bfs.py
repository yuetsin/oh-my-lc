#!/usr/bin/env python

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        queue = list()
        queue.append((root, 1))
        while(len(queue) != 0):
            head, depth = queue.pop(0)
            for i in head.children:
                queue.append((i, depth+1))
        return depth

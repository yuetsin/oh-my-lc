#!/usr/bin/env python

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        return max([1 + self.maxDepth(child) for child in root.children] + [1])

#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def sumUp(self, node: TreeNode) -> int:
        if not node:
            return 0

        return node.val + self.sumUp(node.left) + self.sumUp(node.right)

    def getTilt(self, node: TreeNode) -> int:
        if not node:
            return 0
        return abs(self.sumUp(node.left) - self.sumUp(node.right))

    def findTilt(self, node: TreeNode) -> int:
        if not node:
            return 0
        return self.getTilt(node) + self.findTilt(node.left) + self.findTilt(node.right)

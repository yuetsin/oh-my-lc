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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        @lru_cache(maxsize=None)
        def depth(node: TreeNode) -> int:
            if not node:
                return -1
            return max(depth(node.left), depth(node.right)) + 1

        lr = depth(root.left) + depth(root.right) + 2

        lx = self.diameterOfBinaryTree(root.left)
        rx = self.diameterOfBinaryTree(root.right)

        return max(lr, max(lx, rx))

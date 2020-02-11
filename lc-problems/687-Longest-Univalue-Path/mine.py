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
    def longestUnivaluePath(self, node: TreeNode, canBeRoot: bool = True) -> int:
        if not node:
            return 0
        v = 0
        if canBeRoot:
            if node.left and node.right and node.left.val == node.right.val and node.left.val == node.val:
                # 2, because node - left subtree and node - right subtree has 2 distance
                cur = self.longestUnivaluePath(
                    node.left, False) + self.longestUnivaluePath(node.right, False) + 2
                v = max(v, cur)

            if node.left:
                v = max(v, self.longestUnivaluePath(node.left, True))

            if node.right:
                v = max(v, self.longestUnivaluePath(node.right, True))

        if node.left and node.left.val == node.val:
            v = max(v, 1 + self.longestUnivaluePath(node.left, False))

        if node.right and node.right.val == node.val:
            v = max(v, 1 + self.longestUnivaluePath(node.right, False))

        return v

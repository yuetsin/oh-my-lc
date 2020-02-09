#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        sets = set()

        def traverse(node: TreeNode):
            if not node:
                return

            sets.add(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)

        l = list(sets)
        l.sort()
        if len(l) < 2:
            return -1
        return l[1]

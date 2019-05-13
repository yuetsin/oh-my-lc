#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root):
        self.flag = False
        self.getHeight(root)
        return not self.flag

    def getHeight(self, root):
        if not root:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if abs(left - right) > 1:
            self.flag = True
        return max(left, right) + 1

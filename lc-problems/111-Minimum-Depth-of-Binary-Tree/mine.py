#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1

        vala = self.minDepth(root.left)
        valb = self.minDepth(root.right)
        if vala == 0:
            return valb + 1
        if valb == 0:
            return vala + 1
        return min(vala, valb) + 1

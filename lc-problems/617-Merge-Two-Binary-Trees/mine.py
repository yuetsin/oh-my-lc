#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            newNode = TreeNode(t1.val + t2.val)
            newNode.left = self.mergeTrees(t1.left, t2.left)
            newNode.right = self.mergeTrees(t1.right, t2.right)
            return newNode
        elif t1:
            # t2 is None
            return t1
        elif t2:
            # t1 is None
            return t2
        else:
            # all none
            return None

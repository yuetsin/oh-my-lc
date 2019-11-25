#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumOfLeftLeaves(self, node: TreeNode, isLeft=False) -> int:
        if node == None:
            return 0
        if node.left == None and node.right == None and isLeft:
            return node.val
        return self.sumOfLeftLeaves(node.left, True) + self.sumOfLeftLeaves(node.right, False)

#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, node: TreeNode, val: int) -> TreeNode:
        if not node:
            return None
        this_val = node.val
        if this_val == val:
            return node
        elif this_val < val:
            return self.searchBST(node.right, val)
        elif this_val > val:
            return self.searchBST(node.left, val)
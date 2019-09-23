#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        keys = []

        def traverse(node: TreeNode):
            if node == None:
                return
            keys.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        keys.sort()
        return keys[k - 1]

#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.cur = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.rightMostDfs(root)
        return root

    def rightMostDfs(self, node):
        if node == None:
            return 0

        self.rightMostDfs(node.right)
        node.val += self.cur
        self.cur = node.val
        self.rightMostDfs(node.left)

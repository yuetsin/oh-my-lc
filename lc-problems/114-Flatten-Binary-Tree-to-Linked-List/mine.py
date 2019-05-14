#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preOrder = []

        def findPreOrder(node: TreeNode) -> None:
            if node == None:
                return
            preOrder.append(node)
            findPreOrder(node.left)
            findPreOrder(node.right)

        findPreOrder(root)

        if preOrder == []:
            return

        for i in range(len(preOrder) - 1):
            preOrder[i].left = None
            preOrder[i].right = preOrder[i + 1]

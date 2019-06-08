#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []

        def PO(node: TreeNode):
            if node:
                self.result.append(node.val)
                PO(node.left)
                PO(node.right)
        PO(root)
        return self.result

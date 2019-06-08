#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []

        def PO(node: TreeNode):
            if node:
                PO(node.left)
                PO(node.right)
                self.result.append(node.val)
        PO(root)
        return self.result

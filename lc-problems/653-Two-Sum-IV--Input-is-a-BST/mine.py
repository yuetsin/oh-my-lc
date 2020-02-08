#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        counts = {}

        def traverse(node: TreeNode):
            if not node:
                return

            if node.val in counts:
                counts[node.val] += 1
            else:
                counts.update({
                    node.val: 1
                })

            traverse(node.left)
            traverse(node.right)

        traverse(root)

        for key, val in counts.items():
            target = k - key
            if target == key:
                if val > 1:
                    return True
            else:
                if target in counts:
                    return True
        return False

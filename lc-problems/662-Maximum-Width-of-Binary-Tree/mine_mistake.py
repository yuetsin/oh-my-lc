#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        widths = []

        def traverse(node: TreeNode, depth: int):
            while len(widths) <= depth:
                widths.append([])
            if node:
                widths[depth].append('*')
                traverse(node.left, depth + 1)
                traverse(node.right, depth + 1)
            else:
                widths[depth].append(' ')

        traverse(root, 0)
        widths.pop(-1)

        max_width = 0
        for layer in widths:
            print(''.join(layer).strip())
            max_width = max(max_width, len(''.join(layer).strip()))
        return max_width

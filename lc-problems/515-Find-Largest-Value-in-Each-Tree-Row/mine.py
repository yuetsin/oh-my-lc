#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        layers_max = []

        def traverse(node: TreeNode, layer: int):
            if not node:
                return

            while len(layers_max) <= layer:
                layers_max.append(float('-inf'))

            layers_max[layer] = max(layers_max[layer], node.val)

            traverse(node.left, layer + 1)
            traverse(node.right, layer + 1)

        traverse(root, 0)

        return layers_max

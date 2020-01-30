#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:

        layers = []
        self.deepest_layer = 0

        def traverse(node: TreeNode, depth: int):
            # print("called traverse %s, depth = %d" % (node, depth))
            if not node:
                return
            if depth == self.deepest_layer:
                layers.append(node.val)
            elif depth > self.deepest_layer:
                layers.clear()
                layers.append(node.val)
                self.deepest_layer = depth
            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

        traverse(root, 0)
        # assert that's not null
        return layers[0]

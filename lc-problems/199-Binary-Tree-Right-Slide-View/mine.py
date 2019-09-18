#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.layers = {}

        def iterate(node: TreeNode, layer: int):
            if node == None:
                return
            self.layers.update({layer: node.val})
            iterate(node.left, layer + 1)
            iterate(node.right, layer + 1)
        iterate(root, 0)
        result = []
        for val in self.layers:
            result.append(self.layers[val])
        return result

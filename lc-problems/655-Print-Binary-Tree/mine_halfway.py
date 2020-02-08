#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        layers = []

        def traverse(node: TreeNode, depth: int) -> width:

            while len(layers) <= depth:
                layers.append([])

            if not node:
                layers[depth].append('')
            else:
                layers[depth].append(str(node.val))
                lwdtraverse(node.left, depth + 1)
                traverse(node.right, depth + 1)

        traverse(root, 0)
        layers.pop(-1)

        print(layers)

        layer_cnt = len(layers)

        width = 2 ** layer_cnt - 1

        result = []

        for i in range(layer_cnt):
            layer = layers[i]
            2 ** i

#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        kvmap = {}

        def traverse(node: TreeNode):
            if node:
                if node.val in kvmap:
                    kvmap[node.val] += 1
                else:
                    kvmap.update({
                        node.val: 1
                    })
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        if len(kvmap) == 0:
            return []

        max_v = max([v for k, v in kvmap.items()])

        results = []

        for k, v in kvmap.items():
            if v == max_v:
                results.append(k)

        return results

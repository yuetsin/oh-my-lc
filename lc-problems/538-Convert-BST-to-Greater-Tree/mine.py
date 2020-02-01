#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import bisect


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        all_v = []

        def traverse(node: TreeNode):
            if not node:
                return

            bisect.insort_left(all_v, node.val)

            traverse(node.left)
            traverse(node.right)

        sum_v = []
        last_c = 0

        traverse(root)

        for i in range(len(all_v) - 1, -1, -1):
            last_c += all_v[i]
            sum_v.insert(0, last_c)

        def traverse2(node: TreeNode):
            if not node:
                return

            idx = bisect.bisect_left(all_v, node.val)
            node.val = sum_v[idx]

            traverse2(node.left)
            traverse2(node.right)
        # print(all_v)
        # print(sum_v)

        traverse2(root)

        return root

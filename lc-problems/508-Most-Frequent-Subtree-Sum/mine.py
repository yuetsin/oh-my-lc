#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if root == None:
            return []

        sums = {}

        def getSum(node: TreeNode) -> int:
            if not node:
                return 0
            v = node.val + getSum(node.left) + getSum(node.right)
            if v in sums:
                sums[v] += 1
            else:
                sums.update({
                    v: 1
                })
            return v

        getSum(root)

        max_freq = max([v for k, v in sums.items()])

        result = []

        for k, v in sums.items():
            if v == max_freq:
                result.append(k)
        # print(sums)
        return result

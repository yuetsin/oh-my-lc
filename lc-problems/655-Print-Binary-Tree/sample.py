#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        self.l = self.fl(root)
        res = []
        self.dfs(root, 0, 0, self.l, res)
        return res

    def fl(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        l = max(self.fl(root.left), self.fl(root.right)) * 2 + 1
        return l

    def dfs(self, root, row, left, right, res):
        if root is None:
            return
        if row >= len(res):
            res.append(['' for _ in range(self.l)])
        mid = (left + right) // 2
        res[row][mid] = str(root.val)
        self.dfs(root.left, row+1, left, mid-1, res)
        self.dfs(root.right, row+1, mid+1, right, res)

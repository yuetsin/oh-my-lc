#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        global_rst = []

        def findAll(node: TreeNode, prev: List[int], cursum: int):
            if node == None:
                return
            if node.left == None and node.right == None:
                if cursum == node.val:
                    prev.append(node)
                    global_rst.append([i.val for i in prev])
                return
            findAll(node.left, prev + [node], cursum - node.val)
            findAll(node.right, prev + [node], cursum - node.val)

        findAll(root, [], sum)
        return global_rst

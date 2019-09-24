#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def getTreeChain(current: 'TreeNode', target: 'TreeNode') -> bool:
            if current == None:
                return False
            elif current == target:
                traverse.append(current)
                return True
            if getTreeChain(current.left, target) or getTreeChain(current.right, target):
                traverse.append(current)
                return True
            return False

        traverse = []
        getTreeChain(root, p)
        chainP = traverse
        chainP.reverse()

        traverse = []
        getTreeChain(root, q)
        chainQ = traverse
        chainQ.reverse()
        # print("chain p: ", [node.val for node in chainP])
        # print("chain q: ", [node.val for node in chainQ])
        for i in range(min(len(chainP), len(chainQ)) - 1, -1, -1):
            if chainP[i] == chainQ[i]:
                return chainP[i]

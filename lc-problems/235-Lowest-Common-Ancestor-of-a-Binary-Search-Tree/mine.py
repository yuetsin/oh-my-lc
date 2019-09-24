#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def getTreeChain(target: 'TreeNode') -> List['TreeNode']:

            node = root
            chain = []
            while node != target:
                chain.append(node)
                if node.val < target.val:
                    node = node.right
                else:
                    node = node.left
            chain.append(target)
            return chain

        chainP = getTreeChain(p)
        chainQ = getTreeChain(q)
        # print("chain p: ", chainP)
        # print("chain q: ", chainQ)
        for i in range(min(len(chainP), len(chainQ)) - 1, -1, -1):
            if chainP[i] == chainQ[i]:
                return chainP[i]

#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.frequencyDict = collections.defaultdict(int)
        self.mostCommonCount = 0

        self.getNodeSum(root)
        for k, v in self.frequencyDict.items():
            if v == self.mostCommonCount:
                res.append(k)

        return res

    def getNodeSum(self, node):

        if not node:
            return 0

        leftSum = self.getNodeSum(node.left)
        rightSum = self.getNodeSum(node.right)

        subTreeSum = node.val + leftSum + rightSum
        self.frequencyDict[subTreeSum] += 1
        self.mostCommonCount = max(
            self.frequencyDict[subTreeSum], self.mostCommonCount)
        return subTreeSum

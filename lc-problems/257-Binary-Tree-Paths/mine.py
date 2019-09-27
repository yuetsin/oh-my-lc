#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return []
        lefts = self.binaryTreePaths(root.left)
        rights = self.binaryTreePaths(root.right)

        conseqs = []

        if lefts != [] and rights != []:
            conseqs += ["%d->" % root.val + conseq for conseq in lefts]
            conseqs += ["%d->" % root.val + conseq for conseq in rights]
        elif lefts != []:
            conseqs += ["%d->" % root.val + conseq for conseq in lefts]
        elif rights != []:
            conseqs += ["%d->" % root.val + conseq for conseq in rights]
        else:
            return ["%d" % root.val]

        return conseqs

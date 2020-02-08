#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:

        def stringize(node: TreeNode) -> str:
            if not node:
                return ''

            return "%d(%s)(%s)" % (node.val, stringize(node.left), stringize(node.right))

        existed = set()

        result = set()

        added = set()

        def traverse(node: TreeNode):
            if not node:
                return

            stri = stringize(node)
            if stri != '' and stri in existed:
                if not stri in added:
                    result.add(node)
                    added.add(stri)
            else:
                existed.add(stri)

            traverse(node.left)
            traverse(node.right)

        traverse(root)

        return list(result)

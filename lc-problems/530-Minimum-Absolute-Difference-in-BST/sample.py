#!/usr/bin/env python

# iterative


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        prev = None
        self.min = float('inf')
        stack, inorder = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            while stack:
                root = stack.pop()
                if prev is not None:
                    self.min = min(self.min, root.val - prev)
                prev = root.val
                root = root.right
                if root:
                    break
        return self.min

# recursive


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.prev = None
        self.min = float('inf')

        def recurse(root):
            if root:
                recurse(root.left)
                if self.prev is not None:
                    self.min = min(self.min, root.val-self.prev)
                self.prev = root.val
                recurse(root.right)
        recurse(root)
        return self.min

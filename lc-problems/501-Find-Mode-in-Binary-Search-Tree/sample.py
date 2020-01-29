#!/usr/bin/env python

# recursive
from collections import Counter


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self. prev = None
        self.cur_count = 1
        self.max_count = 0

        if not root:
            return []

        def dfs(node):
            if node:
                dfs(node.left)
                if self.prev is not None:
                    if node.val == self.prev:
                        self.cur_count += 1
                    else:
                        self.cur_count = 1
                self.max_count = max(self.max_count, self.cur_count)
                self.prev = node.val
                dfs(node.right)
        dfs(root)

        result = []
        self.cur_count = 1
        self. prev = None

        def dfs(node):
            if node:
                dfs(node.left)
                if self.prev is not None:
                    if node.val == self.prev:
                        self.cur_count += 1
                    else:
                        self.cur_count = 1
                if self.cur_count == self.max_count:
                    result.append(node.val)
                self.prev = node.val
                dfs(node.right)
        dfs(root)
        return result


# iterative


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        stack = []
        root_p = root
        self. prev = None
        self.cur_count = 1
        self.max_count = 0
        if not root:
            return []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            while stack:
                root = stack.pop()
                if self.prev is not None:
                    if root.val == self.prev:
                        self.cur_count += 1
                    else:
                        self.cur_count = 1
                self.max_count = max(self.max_count, self.cur_count)
                self.prev = root.val
                root = root.right
                if root:
                    break

        self. prev = None
        self.cur_count = 1
        result = []
        while root_p or stack:
            while root_p:
                stack.append(root_p)
                root_p = root_p.left

            while stack:
                root_p = stack.pop()
                if self.prev is not None:
                    if root_p.val == self.prev:
                        self.cur_count += 1
                    else:
                        self.cur_count = 1
                if self.cur_count == self.max_count:
                    result.append(root_p.val)
                self.prev = root_p.val
                root_p = root_p.right
                if root_p:
                    break
        return result

#!/usr/bin/env python

self.ans = 0


def depth(root):
    if not root:
        return 0
    left = depth(root.left)
    right = depth(root.right)
    # path
    self.ans = max(self.ans, left + right)
    # depth
    return max(left, right) + 1


depth(root)
return self.ans

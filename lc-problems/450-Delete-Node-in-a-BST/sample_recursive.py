#!/usr/bin/env python


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return root
        if root.val == key:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            curr = root.right
            x = root.left
            while(x.right is not None):
                x = x.right
            x.right = curr.left
            curr.left = root.left
            return curr

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

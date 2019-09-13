#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.contents = []
        self.isSorted = False
        self.currentIndex = 0
        self.contentLen = 0
        self.addMe(root)

    def addMe(self, node: TreeNode):
        if node == None:
            return
        self.contents.append(node.val)
        if node.left != None:
            self.addMe(node.left)
        if node.right != None:
            self.addMe(node.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.isSorted:
            self.isSorted = True
            self.contents.sort()
            self.contentLen = len(self.contents)
        if self.currentIndex < self.contentLen:
            self.currentIndex += 1
            return self.contents[self.currentIndex - 1]

    def hasNext(self) -> bool:
        if not self.isSorted:
            self.isSorted = True
            self.contents.sort()
            self.contentLen = len(self.contents)

        """
        @return whether we have a next smallest number
        """
        if self.currentIndex < self.contentLen:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

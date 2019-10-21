#!/usr/bin/env python

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):

    array = []

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.array = []

        def addArray(nested):
            if nested.isInteger():
                self.array.append(nested.getInteger())
            else:
                for nest in nested.getList():
                    addArray(nest)

        for nestedInt in nestedList:
            addArray(nestedInt)

        self.cursor = 0

    def next(self):
        """
        :rtype: int
        """
        result = self.array[self.cursor]
        self.cursor += 1
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cursor < len(self.array)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

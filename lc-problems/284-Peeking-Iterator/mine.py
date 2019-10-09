#!/usr/bin/env python

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:

    current = 0
    nums = []

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.current = 0
        self.nums = []

        while iterator.hasNext():
            self.nums.append(iterator.next())

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nums[self.current]

    def next(self):
        """
        :rtype: int
        """
        val = self.nums[self.current]
        self.current += 1
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.current < len(self.nums)


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

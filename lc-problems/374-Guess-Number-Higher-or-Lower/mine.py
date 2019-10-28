#!/usr/bin/env python

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def tryGuess(start, end):
            # in python i don't worry about overflow
            mid = (start + end) // 2
            rs = guess(mid)
            if rs == 1:
                return tryGuess(mid, end + 1)
            elif rs == -1:
                return tryGuess(start, mid)
            else:
                return mid

        return tryGuess(1, n + 1)

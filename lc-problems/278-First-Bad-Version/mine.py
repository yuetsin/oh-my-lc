#!/usr/bin/env python

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        knownMinBad = n
        knownMaxGood = -1
        while knownMinBad > knownMaxGood + 1:
            point = (knownMinBad + knownMaxGood) // 2
            if isBadVersion(point):
                knownMinBad = point
            else:
                knownMaxGood = point
        return knownMinBad

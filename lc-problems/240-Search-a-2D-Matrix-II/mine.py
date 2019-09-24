#!/usr/bin/env python


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            for j in i:
                if j == target:
                    return True
                elif j > target:
                    continue
        return False

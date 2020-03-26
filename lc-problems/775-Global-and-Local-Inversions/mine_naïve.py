#!/usr/bin/env python


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:

        for i, v in enumerate(A):
            if abs(i - v) > 1:
                return False

        return True

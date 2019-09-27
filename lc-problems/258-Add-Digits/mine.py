#!/usr/bin/env python


class Solution:

    def addDigits(self, num: int) -> int:
        sumUp = sum([int(digit) for digit in str(num)])
        if sumUp < 10:
            return sumUp
        return self.addDigits(sumUp)

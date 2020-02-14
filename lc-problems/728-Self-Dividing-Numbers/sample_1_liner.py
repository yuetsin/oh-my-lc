#!/usr/bin/env python


class Solution:
    def selfDividingNumbers(self, left, right):
        return [number for number in range(left, right+1) if '0' not in str(number) and all((number % int(char) == 0 for char in str(number)))]

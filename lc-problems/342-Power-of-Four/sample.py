#!/usr/bin/env python

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
      return num & (num - 1) == 0 and (list(str(bin(num))).count('0') - 1) % 2 == 0
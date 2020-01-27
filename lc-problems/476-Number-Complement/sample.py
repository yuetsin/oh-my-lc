#!/usr/bin/env python


class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join(chr(97 - ord(ch)) for ch in bin(num)[2:]), 2)

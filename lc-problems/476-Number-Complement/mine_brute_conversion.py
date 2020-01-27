#!/usr/bin/env python


class Solution:
    def findComplement(self, num: int) -> int:
        comp = []
        for char in bin(num)[2:]:
            comp.append('0' if char == '1' else '1')
        comp_str = ''.join(comp)
        return int(comp_str, 2)

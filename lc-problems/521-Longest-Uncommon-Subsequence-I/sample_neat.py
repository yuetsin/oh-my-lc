#!/usr/bin/env python


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return max(len(a), len(b))
        return -1 if a == b else len(a)

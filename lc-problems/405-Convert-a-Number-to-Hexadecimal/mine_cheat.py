#!/usr/bin/env python


class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num += 4294967296
        return "%x" % num

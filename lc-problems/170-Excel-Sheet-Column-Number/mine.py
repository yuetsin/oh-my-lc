#!/usr/bin/env python


class Solution:
    def titleToNumber(self, s: str) -> int:
        strlen = len(s)
        if strlen == 0:
            return 1

        result = 0

        counter = 0
        for i in range(strlen - 1, -1, -1):
            result += ((ord(s[i]) - 64) * pow(26, counter))
            counter += 1

        return result

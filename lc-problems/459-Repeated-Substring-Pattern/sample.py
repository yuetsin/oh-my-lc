#!/usr/bin/env python


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        print(s)
        l = len(s)
        counter = 1
        while counter <= l/2:
            substring = s[:counter]
            if s.count(substring) == l/counter:
                return True
            counter += 1
        return False

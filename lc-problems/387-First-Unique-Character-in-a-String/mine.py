#!/usr/bin/env python


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = 0
        duplicated = set()
        for ch in s:
            if ch in duplicated:
                counter += 1
                continue
            if s.count(ch) == 1:
                return counter
            duplicated.add(ch)
            counter += 1
        return -1

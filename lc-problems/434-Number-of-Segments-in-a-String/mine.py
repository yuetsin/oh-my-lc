#!/usr/bin/env python


class Solution:
    def countSegments(self, s: str) -> int:
        return len([v for v in s.split(' ') if v != ''])

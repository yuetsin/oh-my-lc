#!/usr/bin/env python


class Solution:
    def reverseWords(self, s: str) -> str:
        l = [l for l in s.split(' ') if len(l)]
        l.reverse()
        return ' '.join(l)

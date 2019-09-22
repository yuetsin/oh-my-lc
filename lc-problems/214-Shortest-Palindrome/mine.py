#!/usr/bin/env python


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def isPalind(s: str) -> bool:
            return s == s[::-1]
        if isPalind(s):
            return s
        strlen = len(s)
        for i in range(1, len(s)):
            combination = s[:(strlen - i) - 1:-1] + s
            if isPalind(combination):
                return combination

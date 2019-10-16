#!/usr/bin/env python


class Solution:
    def reverseVowels(self, s: str) -> str:
        lptr = 0
        rptr = len(s) - 1

        vowels = "aeiouAEIOU"

        s = list(s)

        while lptr < rptr:
            if s[lptr] in vowels and s[rptr] in vowels:
                s[lptr], s[rptr] = s[rptr], s[lptr]
                lptr += 1
                rptr -= 1

            if not s[lptr] in vowels:
                lptr += 1

            if not s[rptr] in vowels:
                rptr -= 1

        return ''.join(s)

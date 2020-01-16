#!/usr/bin/env python


class Solution:
    def longestPalindrome(self, s: str) -> int:

        if s == '':
            return 0

        ch_count = {}

        for ch in s:
            if ch in ch_count:
                ch_count[ch] += 1
            else:
                ch_count.update({
                    ch: 1
                })

        # print(ch_count)
        stripped = True
        total_even = 0
        for _, count in ch_count.items():
            if count % 2 == 1:
                stripped = False
                total_even += count - 1
            else:
                total_even += count

        return total_even if stripped else total_even + 1

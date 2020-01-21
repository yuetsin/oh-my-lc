#!/usr/bin/env python


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = collections.Counter(s)
        freq = {k: v for k, v in sorted(
            freq.items(), key=lambda item: item[1], reverse=True)}
        return ''.join([k * v for k, v in freq.items()])

#!/usr/bin/env python


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.reverse()
        return sum(i < j for i, j in enumerate(citations))

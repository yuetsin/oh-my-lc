#!/usr/bin/env python


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if words == []:
            return []

        freq = dict(collections.Counter(words))

        items = freq.items()
        items = sorted(items, key=lambda v: (-v[1], v[0]))

        return [k for k, _ in items[:k]]

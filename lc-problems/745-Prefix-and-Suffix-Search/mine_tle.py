#!/usr/bin/env python

from functools import lru_cache


class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words

    @lru_cache(maxsize=None)
    def f(self, prefix: str, suffix: str) -> int:

        for i in range(len(self.words) - 1, -1, -1):
            word = self.words[i]
            if word.startswith(prefix) and word.endswith(suffix):
                return i

        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

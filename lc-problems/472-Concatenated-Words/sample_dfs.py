#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        words = set(words)

        @lru_cache(maxsize=10000)
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in words and suffix in words:
                    return True

                if prefix in words and dfs(suffix):
                    return True

            return False

        return [word for word in words if dfs(word)]

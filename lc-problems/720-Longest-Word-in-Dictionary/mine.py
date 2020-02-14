#!/usr/bin/env python


class Solution:
    def longestWord(self, words: List[str]) -> str:

        if not words:
            return ''

        words.sort(key=lambda s: len(s))

        buildable = set()

        for word in words:
            if len(word) < 2:
                buildable.add(word)
            elif word[:-1] in buildable:
                buildable.add(word)

        maxl = max([len(s) for s in buildable])

        result = []

        for w in buildable:
            if len(w) == maxl:
                result.append(w)

        result.sort()
        return result[0]

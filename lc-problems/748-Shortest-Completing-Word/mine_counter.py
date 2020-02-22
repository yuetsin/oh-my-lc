#!/usr/bin/env python

from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        given = dict(Counter(licensePlate.lower()))

        words.sort(key=lambda m: len(m))

        for word in words:
            current = dict(Counter(word.lower()))

            ok = True

            for k, v in given.items():
                if k.isalpha():
                    if k in current and current[k] >= v:
                        continue
                    else:
                        ok = False
                        break

            if ok:
                return word

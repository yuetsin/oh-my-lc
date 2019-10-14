#!/usr/bin/env python


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        wordsCount = len(words)
        sets = []
        length = []
        for word in words:
            sets.append(set(list(word)))
            length.append(len(word))

        result = 0
        for i in range(wordsCount):
            for j in range(i + 1, wordsCount):
                if sets[i].intersection(sets[j]):
                    continue
                result = max(result, length[i] * length[j])

        return result

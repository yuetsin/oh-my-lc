#!/usr/bin/env python


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        word_c = len(words)

        def isPalid(word: str) -> bool:
            return word == word[::-1]

        results = []
        for i in range(word_c):
            for j in range(i + 1, word_c):
                if isPalid(words[i] + words[j]):
                    results.append([i, j])
                if isPalid(words[j] + words[i]):
                    results.append([j, i])

        return results

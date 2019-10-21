#!/usr/bin/env python


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        dicts = {}
        for i, word in enumerate(words):
            dicts[word[::-1]] = i

        def isPalindrome(s):
            return s == s[::-1]

        res = set()
        for i, word in enumerate(words):

            for j in range(len(word)+1):  # to cover the case of empty string
                left = word[:j]
                right = word[j:]
                # case 1:
                if isPalindrome(left) and (right in dicts) and (i != dicts[right]):
                    res.add((dicts[right], i))
                # case 2:
                if isPalindrome(right) and (left in dicts) and (i != dicts[left]):
                    res.add((i, dicts[left]))
        return res

#!/usr/bin/env python


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def normalized(s: str):
            dictionary = []
            result = []
            for i in s:
                if i in dictionary:
                    result.append(dictionary.index(i))
                else:
                    dictionary.append(i)
                    result.append(len(dictionary) - 1)
            return result
        return normalized(s) == normalized(t)

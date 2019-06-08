#!/usr/bin/env python
#
#
# This Solution Failed at Test Case #30:
# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict

        def find_possible_following(s: str) -> List[str]:
            rst = []
            for word in self.wordDict:
                if s[:len(word)] == word:
                    rst.append(s[len(word):])
            return rst

        def findPos(s: str) -> bool:
            if len(s) == 0:
                return True
            for i in find_possible_following(s):
                if findPos(i):
                    return True

            return False

        return findPos(s)

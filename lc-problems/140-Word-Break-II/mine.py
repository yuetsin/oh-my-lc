#!/usr/bin/env python


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.s = s
        self.s_len = len(s)
        self.DP = {}
        self.wordDict = wordDict

        def find_possible_following(s_idx: int):
            rst = []
            find_words = []
            for word in self.wordDict:
                if s[s_idx:].startswith(word):
                    rst.append(len(word) + s_idx)
                    find_words.append(word)
            return rst, find_words

        def findPos(s_idx: int) -> List[List[str]]:
            if not s_idx in self.DP:
                real_rst = []
                if s_idx >= self.s_len:
                    return [[]]
                else:
                    indexes, words = find_possible_following(s_idx)
                    for i in range(len(indexes)):
                        rst = findPos(indexes[i])
                        if rst != []:
                            for itm in rst:
                                real_rst.append([words[i]] + itm)
                self.DP.update({s_idx: real_rst})
            return self.DP[s_idx]
        return [' '.join(s) for s in findPos(0)]

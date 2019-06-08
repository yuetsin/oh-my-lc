#!/usr/bin/env python


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.s_len = len(s)
        self.DP = {}
        self.wordDict = wordDict

        def find_possible_following(s_idx: int) -> List[int]:
            rst = []
            for word in self.wordDict:
                if s[s_idx:].startswith(word):
                    rst.append(len(word) + s_idx)
            return rst

        def findPos(s_idx: int) -> bool:
            if not s_idx in self.DP:
                if s_idx >= self.s_len:
                    self.DP.update({s_idx: True})
                else:
                    for i in find_possible_following(s_idx):
                        if findPos(i):
                            self.DP.update({s_idx: True})
                            break
                    if not s_idx in self.DP:
                        self.DP.update({s_idx: False})
            return self.DP[s_idx]
        return findPos(0)

#!/usr/bin/env python


class Solution:
    def makeLargestSpecial(self, S: str) -> str:

        self.i = 0

        def dfs() -> str:

            res = []
            toks = []

            while self.i < len(S) and res == []:
                if S[self.i] == '1':
                    self.i += 1
                    toks.append(dfs())
                else:
                    self.i += 1
                    res.append('1')

            prefix = len(res)

            toks.sort(reverse=True)
            res += toks

            if prefix > 0:
                res.append('0')

            # print("res = ", res)
            # print("toks = ", toks)
            return ''.join(res)

        return dfs()

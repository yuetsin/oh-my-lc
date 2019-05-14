#!/usr/bin/env python


class Solution:

    global_cnt = 0

    DP = {}

    def numDistinct(self, s: str, t: str) -> int:
        self.global_cnt = 0
        self.DP = {}
        slen = len(s)
        tlen = len(t)

        def getSince(sptr: int, tptr: int) -> int:

            if not (sptr, tptr) in self.DP:
                if tptr == tlen:
                    self.DP.update({(sptr, tptr): 1})
                    return 1

                if sptr == slen:
                    self.DP.update({(sptr, tptr): 0})
                    return 0

                rst = 0
                if s[sptr] == t[tptr]:
                    rst += getSince(sptr + 1, tptr + 1)

                rst += getSince(sptr + 1, tptr)
                self.DP.update({(sptr, tptr): rst})
            return self.DP[(sptr, tptr)]

        return getSince(0, 0)

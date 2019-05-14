#!/usr/bin/env python


class Solution:

    global_cnt = 0

    def numDistinct(self, s: str, t: str) -> int:

        slen = len(s)
        tlen = len(t)

        def getSince(sptr: int, tptr: int) -> int:

            if tptr == tlen:
                return 1

            if sptr == slen:
                return 0

            rst = 0
            if s[sptr] == t[tptr]:
                rst += getSince(sptr + 1, tptr + 1)

            rst += getSince(sptr + 1, tptr)
            return rst

        return getSince(0, 0)

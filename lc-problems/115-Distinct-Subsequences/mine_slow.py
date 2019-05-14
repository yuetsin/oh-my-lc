#!/usr/bin/env python


class Solution:

    global_cnt = 0

    def numDistinct(self, s: str, t: str) -> int:

        slen = len(s)
        tlen = len(t)

        def getSince(sptr: int, tptr: int) -> None:

            if tptr == tlen:
                self.global_cnt += 1
                return

            if sptr == slen:
                return

            if s[sptr] == t[tptr]:
                getSince(sptr + 1, tptr + 1)

            getSince(sptr + 1, tptr)

        getSince(0, 0)

        return self.global_cnt

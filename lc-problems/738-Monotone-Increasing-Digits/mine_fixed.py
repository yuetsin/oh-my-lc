#!/usr/bin/env python


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        ans = list(str(N))
        lenn = len(ans)
        idx = lenn
        for i in range(lenn - 2, -1, -1):
            if ans[i] > ans[i + 1]:
                idx = i + 1
                ans[i] = chr(ord(ans[i]) - 1)

        for i in range(idx, lenn):
            ans[i] = '9'

        return int(''.join(ans))

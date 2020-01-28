#!/usr/bin/env python
#
# by @nuclearoreo


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = ''.join(S.upper().split('-'))
        remainder, res = len(S) % K, []

        if remainder > 0:
            res.append(S[:remainder])
            S = S[remainder:]

        for i in range(0, len(S), K):
            res.append(S[i:i+K])

        return '-'.join(res)

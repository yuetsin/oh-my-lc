#!/usr/bin/env python


class Solution:

    def swap(self, stri: str) -> str:
        if len(stri) < 2:
            return stri

        v = list(stri)
        max_v = max(v)
        max_v_i = stri.rfind(max_v)
        if v[max_v_i] == v[0]:
            return stri[0] + self.swap(stri[1:])

        v[max_v_i], v[0] = v[0], v[max_v_i]
        return ''.join(v)

    def maximumSwap(self, num: int) -> int:
        return int(self.swap(str(num)))

#!/usr/bin/env python


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = ""

        for d in num:
            while k > 0 and len(st) > 0 and st[-1] > d:
                st = st[:-1]
                k -= 1

            st += d

        st = st[:-k] if k > 0 else st
        return st.lstrip('0') or "0"

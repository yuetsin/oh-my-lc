#!/usr/bin/env python


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return ''.join(s[i*k:(i+1)*k] if i % 2 else s[i*k:(i+1)*k][::-1] for i in range(len(s)//k + 1))

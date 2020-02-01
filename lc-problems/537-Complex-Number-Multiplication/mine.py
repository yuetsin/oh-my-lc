#!/usr/bin/env python


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_s = a.split('+')
        b_s = b.split('+')

        a_r, a_i = int(a_s[0]), int(a_s[1][:-1])
        b_r, b_i = int(b_s[0]), int(b_s[1][:-1])

        real = a_r * b_r - a_i * b_i
        fake = a_r * b_i + a_i * b_r

        return "%d+%di" % (real, fake)

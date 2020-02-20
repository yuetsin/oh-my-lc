#!/usr/bin/env python


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        digits = []
        A = map(int, str(N))
        for i in xrange(len(A)):
            for d in xrange(1, 10):
                if digits + [d] * (len(A)-i) > A:
                    digits.append(d-1)
                    break
            else:
                digits.append(9)

        return int("".join(map(str, digits)))

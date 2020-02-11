#!/usr/bin/env python


class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:

        if len(B) == 0:
            return 0
        begin_chr = B[0]

        startpoints = []

        for i in range(len(A)):
            if A[i] == begin_chr:
                startpoints.append(i)

        if len(startpoints) == 0:
            # N/E
            return -1

        times = float('+inf')

        lena = len(A)
        for sp in startpoints:
            ok = True
            i = sp
            counter = 1
            for char in B:
                if i >= lena:
                    i = 0
                    counter += 1
                if char != A[i]:
                    ok = False
                    break
                i += 1

            if ok:
                times = min(times, counter)

        return times if times != float('+inf') else -1

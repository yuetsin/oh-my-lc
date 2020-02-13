#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:

        lena = len(A)
        lenb = len(B)

        if A == B:
            return lena

        @lru_cache(maxsize=None)
        def length(ai: int, bi: int) -> int:
            oai, obi = ai, bi
            # print("called length(%d, %d)" % (ai, bi))
            if ai >= lena or bi >= lena:
                return 0

            counter = 0

            saeko = True
            while ai < lena and bi < lenb:
                if A[ai] == B[bi]:
                    ai += 1
                    bi += 1
                    counter += 1
                else:
                    saeko = False
                    break

            if saeko:
                return counter
            else:
                return max(counter, length(oai + 1, obi), length(oai, obi + 1))

        return length(0, 0)

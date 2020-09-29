#!/usr/bin/env python3

class Solution:
    def rotateString(self, A: str, B: str) -> bool:

        if A == '' and B == '':
            return True

        # 长度最多 100？那这不是随便写？
        for i in range(1, len(A)):
            shift = A[i:] + A[:i]
            if shift == B:
                return True
        return False

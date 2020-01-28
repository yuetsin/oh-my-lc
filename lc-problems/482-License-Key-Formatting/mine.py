#!/usr/bin/env python


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        codes = list(S.replace('-', '').upper())
        size = len(codes)

        if size % K != 0:
            for _ in range(K - size % K):
                codes.insert(0, '')

        # print(codes)

        new_size = len(codes)

        parts = []
        for joint in range(new_size // K):
            # print(joint)
            parts.append(''.join(codes[joint * K: (joint + 1) * K]))
        return '-'.join(parts)

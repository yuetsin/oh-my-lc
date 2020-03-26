#!/usr/bin/env python


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(J)
        return len([v for v in S if v in J])

#!/usr/bin/env python


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        seq = sorted((e[0], i) for i, e in enumerate(intervals))
        return [seq[loc][1] if (loc:=bisect.bisect_left(seq, (e[1],))) < len(intervals) else -1 for e in intervals]

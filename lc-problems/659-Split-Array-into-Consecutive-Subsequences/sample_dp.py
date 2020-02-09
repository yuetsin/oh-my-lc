#!/usr/bin/env python

# written by @dpwang


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        d = collections.defaultdict(list)
        for e in nums:
            if d[e-1]:  # there is sequence ending with e-1
                l = heapq.heappop(d[e-1])  # the shortest sequence
                heapq.heappush(d[e], l+1)
            else:
                heapq.heappush(d[e], 1)  # create a new sequence
        for h in d.values():
            for hl in h:
                if hl < 3:
                    return False
        return True

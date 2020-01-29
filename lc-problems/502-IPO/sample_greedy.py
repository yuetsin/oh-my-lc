#!/usr/bin/env python

import heapq


class Solution(object):
    def findMaximizedCapital(self, k, oc, ps, cs):
        l, i, heap = zip(cs, ps), 0, []
        l.sort()
        while(k):
            while(i < len(l) and l[i][0] <= oc):
                heapq.heappush(heap, -l[i][1])
                i += 1
            if heap:
                k -= 1
                oc += -heapq.heappop(heap)
            else:
                break
        return oc

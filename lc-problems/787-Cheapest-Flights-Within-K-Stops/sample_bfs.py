#!/usr/bin/env python3

from collections import defaultdict, deque

# written by @ggyc1993


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph, res, q, visisted = defaultdict(list), float(
            'inf'), deque([(src, 0, 0)]), set([])
        for f in flights:
            graph[f[0]].append((f[1], f[2]))
        while q:
            cur_flight, lvl, price = q.popleft()
            if lvl > K + 1:
                break
            if cur_flight == dst:
                res = min(res, price)
            for next_flight, flight_price in graph[cur_flight]:
                if flight_price + price >= res:
                    continue
                q.append((next_flight, lvl + 1, flight_price + price))
        return res if res != float('inf') else -1

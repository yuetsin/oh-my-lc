#!/usr/bin/env python

import heapq
from typing import List, Tuple
from itertools import islice


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        # Generator to generate pairs
        def gen_pairs():
            for i in nums1:
                for j in nums2:
                    yield (i, j)

        max_heap: List[Tuple[int, List[int]]] = []

        gen = gen_pairs()

        # Consume the first K pairs
        for i, j in islice(gen, k):
            heapq.heappush(max_heap, (-(i+j), [i, j]))

        # For the remaining pairs, evict everytime you push.
        # Evict the pair with maximum sum.
        for i, j in gen:
            heapq.heappushpop(max_heap, (-(i+j), [i, j]))

        # Remaining items in the max heap are the K smallest pairs.
        return [item[1] for item in max_heap]

#!/usr/bin/env python


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        times = {}

        for num in nums:
            if num in times:
                times[num] += 1
            else:
                times.update({
                    num: 1
                })

        return sorted(times, key=times.__getitem__, reverse=True)[:k]

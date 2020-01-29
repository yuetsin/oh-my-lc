#!/usr/bin/env python


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        last_stop = 0
        total = 0
        for num in timeSeries:
            if last_stop < num:
                total += duration
            else:
                total += duration + (num - last_stop)
            last_stop = num + duration

        return total

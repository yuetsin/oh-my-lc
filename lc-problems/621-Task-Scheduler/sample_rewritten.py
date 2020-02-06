#!/usr/bin/env python


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        mapp = [0] * 26
        for ch in tasks:
            mapp[ord(ch) - ord('A')] += 1

        # Actually, letters doesn't matter.
        # Just cares about its occuring frequency.
        mapp.sort()

        max_val = mapp[25] - 1
        idle_slots = max_val * n

        for i in range(24, -1, -1):
            if mapp[i] <= 0:
                break
            idle_slots -= min(mapp[i], max_val)

        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)

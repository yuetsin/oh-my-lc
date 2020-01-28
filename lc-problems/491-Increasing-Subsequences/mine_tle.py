#!/usr/bin/env python

from copy import deepcopy


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        results = []

        results = [[]]

        for new_num in nums:
            results += [deepcopy(v) for v in results]
            halfway = len(results) // 2
            for i in range(len(results)):
                if i < halfway:
                    results[i].append(new_num)

        real_results = []

        for entry in results:
            if len(entry) >= 2 and not entry in real_results:
                ok = True
                for i in range(len(entry) - 1):
                    if entry[i + 1] < entry[i]:
                        ok = False
                        break
                if ok:
                    real_results.append(entry)

        # print(real_results)
        return real_results

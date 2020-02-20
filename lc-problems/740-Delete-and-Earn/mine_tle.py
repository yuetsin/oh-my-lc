#!/usr/bin/env python

from copy import deepcopy
from functools import lru_cache
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dAE(nums: tuple) -> int:
            nums = dict(nums)
            if len(nums) == 0:
                return 0
            ret = 0

            for k, v in nums.items():
                new = deepcopy(nums)

                if new[k] == 1:
                    del new[k]
                else:
                    new[k] -= 1

                if k - 1 in new:
                    del new[k - 1]

                if k + 1 in new:
                    del new[k + 1]

                ret = max(ret, k + dAE(tuple(new.items())))

            return ret

        dd = dict(Counter(nums))

        tups = []

        for k, v in dd.items():
            tups.append((k, v))

        return dAE(tuple(dict(Counter(nums)).items()))

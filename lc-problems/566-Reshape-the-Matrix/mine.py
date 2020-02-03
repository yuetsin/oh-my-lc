#!/usr/bin/env python

import numpy as np


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        r1 = len(nums)
        if not r1:
            return nums

        c1 = len(nums[0])

        if r1 * c1 != r * c:
            return nums

        return np.resize(nums, (r, c))

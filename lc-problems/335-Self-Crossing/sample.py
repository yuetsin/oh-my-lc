#!/usr/bin/env python


class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        n = len(x)

        def helper(i):
            steps = [x[k+i] if k+i < n else 0 for k in range(6)]
            if steps[3] < steps[1]:
                return False
            if steps[2] <= steps[0]:
                return True
            if steps[3] >= steps[1] and steps[4] >= (steps[2]-steps[0]) and steps[4] <= steps[2] and steps[5] >= (steps[3]-steps[1]):
                return True
            return False
        return any(helper(i) for i in range(n-3))

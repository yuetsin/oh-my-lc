#!/usr/bin/env python


class Solution:
    def Backtrack(self, nums: List[int], ind: int) -> int:
        x = ind + 1
        if len(nums) == 1:
            if x % nums[0] == 0 or nums[0] % x == 0:
                return 1
            return 0
        Sum = 0
        for i in range(len(nums)):
            if nums[i] % x == 0 or x % nums[i] == 0:
                Sum = Sum + self.Backtrack(nums[:i] + nums[i + 1:], x)
        return Sum

    def countArrangement(self, N: int) -> int:
        L = []
        for i in range(N):
            L.append(i + 1)
        return self.Backtrack(L, 0)

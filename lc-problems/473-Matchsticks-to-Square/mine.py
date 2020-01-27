#!/usr/bin/env python


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if nums == []:
            return False

        nums.sort(reverse=True)
        sumup = sum(nums)
        numcnts = len(nums)

        if sumup % 4 != 0:
            return False

        target = sumup // 4

        if nums[0] > target:
            return False

        lines = [0, 0, 0, 0]

        def dfs(idx: int) -> bool:
            if idx == numcnts:
                return lines[0] == lines[1] and lines[1] == lines[2] and lines[2] == lines[3]

            for i in range(4):
                if lines[i] + nums[idx] <= target:
                    lines[i] += nums[idx]
                    if dfs(idx + 1):
                        return True
                    lines[i] -= nums[idx]

            return False

        return dfs(0)

#!/usr/bin/env python


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, sums = 0, 0
        maps = {
            0: 1
        }

        for i in range(len(nums)):
            sums += nums[i]
            if sums - k in maps:
                count += maps[sums - k]
            if sums in maps:
                maps[sums] += 1
            else:
                maps.update({
                    sums: 1
                })

        return count

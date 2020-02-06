#!/usr/bin/env python


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minx = 0
        miny = float('+inf')
        nextt = [0] * len(nums)

        flag = True

        for i in range(len(nums)):
            if not flag:
                break

            for j in range(len(nums[i])):
                if not flag:
                    break
                min_i = 0
                max_i = 0
                for k in range(len(nums)):
                    if nums[min_i][nextt[min_i]] > nums[k][nextt[k]]:
                        min_i = k
                    if nums[max_i][nextt[max_i]] < nums[k][nextt[k]]:
                        max_i = k

                if miny - minx > nums[max_i][nextt[max_i]] - nums[min_i][nextt[min_i]]:
                    miny = nums[max_i][nextt[max_i]]
                    minx = nums[min_i][nextt[min_i]]
                nextt[min_i] += 1
                if nextt[min_i] == len(nums[min_i]):
                    flag = False

        return [minx, miny]

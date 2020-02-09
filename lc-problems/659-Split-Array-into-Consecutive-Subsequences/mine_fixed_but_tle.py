#!/usr/bin/env python


class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        arrays = []

        numlen = len(nums)

        def tryit(since: int) -> bool:
            if since == numlen:

                for arr in arrays:
                    if len(arr) <= 2:
                        return False

                # print(arrays)
                return True

            num = nums[since]

            for arr in arrays:
                if len(arr) < 1 or 1 == num - arr[-1]:
                    # cannot build the regulations
                    arr.append(num)
                    if tryit(since + 1):
                        return True

                    arr.pop(-1)

            arrays.append([num])
            result = tryit(since + 1)
            arrays.pop(-1)

            return result

        b = tryit(0)
        return b

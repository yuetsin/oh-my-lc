#!/usr/bin/env python


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        DP = {}

        def coin(nums: tuple) -> int:
            if len(nums) == 1:
                # print("coin: ", nums, " => ", nums[0], "single")
                return nums[0]
            if nums in DP:
                # print("coin: ", nums, " => ", DP[nums], "cached")
                return DP[nums]
            maxC = 0
            for i in range(len(nums)):
                if i == 0:
                    psb = nums[i] * nums[i + 1]
                elif i == len(nums) - 1:
                    psb = nums[i] * nums[i - 1]
                else:
                    psb = nums[i - 1] * nums[i] * nums[i + 1]

                rst = psb + coin(nums[:i] + nums[i+1:])

                maxC = max(maxC, rst)

            DP.update({
                nums: maxC
            })

            # print("coin: ", nums, " => ", maxC)
            return maxC

        return coin(tuple(nums))

#!/usr/bin/env python


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if (k == 0):
            if (len(nums) >= 2):
                for index in range(1, len(nums)):
                    if (nums[index] == 0 and nums[index - 1] == 0):
                        return True

            return False

        if (k < 0):
            k = -k

        sums = {}
        sum_ = 0
        maximum = -2 ** 31
        zero_occured = False
        counter = 0

        for index, number in enumerate(nums):
            if (number == 0):
                if (zero_occured):
                    return True

                zero_occured = True
            else:
                zero_occured = False

            sum_ += number
            counter += 1
            n = sum_ // k * k

            if (not sum_ % k and counter >= 2):
                return True

            required_sum = sum_ - n

            while (n > 0 and required_sum <= maximum):
                if (required_sum in sums and index - sums[required_sum] > 1):
                    return True

                required_sum = sum_ - n
                n -= k

            if (sum_ > maximum):
                maximum = sum_

            if (sum_ not in sums):
                sums[sum_] = index

        return False

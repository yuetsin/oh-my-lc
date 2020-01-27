#!/usr/bin/env python

from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = 0
        masks = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288,
                 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]
        for mask in masks:
            if x & mask != y & mask:
                hamming_distance += 1

        return hamming_distance

    def totalHammingDistance(self, nums: List[int]) -> int:
        result = 0
        for i1 in range(len(nums) - 1):
            for i2 in range(i1 + 1, len(nums)):
                # print(i1, i2)
                result += self.hammingDistance(nums[i1], nums[i2])
        return result

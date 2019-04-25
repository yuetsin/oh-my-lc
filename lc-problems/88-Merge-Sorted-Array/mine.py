#!/usr/bin/env python


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        std = sorted(nums1[:m] + nums2[:n])

        for i in range(len(std)):
            nums1[i] = std[i]

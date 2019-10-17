#!/usr/bin/env python

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    result.append(i)
                    nums2.remove(i)
                    break
        return result
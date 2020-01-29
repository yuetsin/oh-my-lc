#!/usr/bin/env python


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2len = len(nums2)

        results = []
        for num1 in nums1:
            cors = nums2.index(num1)

            found = False
            for i in range(cors + 1, num2len):
                if nums2[i] > num1:
                    results.append(nums2[i])
                    found = True
                    break

            if not found:
                results.append(-1)

        return results

#!/usr/bin/env python


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic.update({num: 1})

        result = []
        limit = len(nums) // 3
        for i in dic:
            if dic[i] > limit:
                result.append(i)
        return result

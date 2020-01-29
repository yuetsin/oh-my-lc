#!/usr/bin/env python
'''
Extend the string by itself to cover circular case.
Use a mono-decreasing stack to store value and idx pair.
When a larger number comes in, pop out smaller numbers before it.
These smaller numbers that got popped out have next larger number of this larger number.
Time: O(n)
Space: O(n)
'''


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        my_stack = []
        nums_len = len(nums)
        nums += nums
        res = [-1]*len(nums)
        for idx, n in enumerate(nums):
            while my_stack and n > my_stack[-1][0]:
                val, i = my_stack.pop()
                res[i] = n
            my_stack += [(n, idx)]
        return res[:nums_len]

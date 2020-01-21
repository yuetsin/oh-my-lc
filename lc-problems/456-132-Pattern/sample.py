#!/usr/bin/env python


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # use a min heap instead of stack to save the potential k value
        # https://leetcode.com/problems/132-pattern/discuss/432266/Python-Different-approach-explained-(array-%2B-heap).-O(n-log-n)
        if len(nums) < 3:
            return False
        min_arr = [None for _ in range(len(nums))]
        min_arr[0] = nums[0]
        stack = []  # a sorted stack by default
        for i in range(1, len(nums)):
            min_arr[i] = min(min_arr[i-1], nums[i])
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > min_arr[j]:
                while stack and stack[-1] <= min_arr[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                # nums[j]<=stack[-1], so the stack remains sorted by default
                stack.append(nums[j])
            else:
                # nums[j]==min_arr[j]
                # so that nums[j]<=min_arr[k], for k<j, because min_arr is in
                # descending order
                pass
        return False

#!/usr/bin/env python

import heapq


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # run time : O(N*log M) where N = total nums, M is len(nums)
        rangeStart = 0
        rangeEnd = float('inf')
        currentMax = float('-inf')
        heap = []

        # put one number from each of k list
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], 0, i))
            currentMax = max(currentMax, nums[i][0])

        # take the smallest(top) element form the min heap,
        # if it gives us smaller range, update the ranges
        # if the array of the top element has more elements,
        # insert the next element in the heap
        while len(heap) == len(nums):
            num, idx, row = heapq.heappop(heap)

            if rangeEnd - rangeStart > currentMax - num:
                rangeStart = num
                rangeEnd = currentMax

            if idx + 1 < len(nums[row]):
                heapq.heappush(heap, (nums[row][idx+1], idx+1, row))
                currentMax = max(currentMax, nums[row][idx+1])

        return [rangeStart, rangeEnd]

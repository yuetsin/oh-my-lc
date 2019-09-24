#!/usr/bin/env python


def maxSlidingWindow(self, nums, k):
    queue = collections.deque([])
    res = []
    for i in range(len(nums)):
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()
        queue.append(i)

        if queue[0] <= i - k:
            queue.popleft()

        if i >= k - 1:
            res.append(nums[queue[0]])

    return res

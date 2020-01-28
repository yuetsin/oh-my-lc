#!/usr/bin/env python

import heapq


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        self.minHeap = []
        self.maxHeap = []
        result = []

        # start adding the nums to min and max heaps
        for i in range(len(nums)):

            if not self.maxHeap or -self.maxHeap[0] >= nums[i]:
                heapq.heappush(self.maxHeap, -nums[i])
            else:
                heapq.heappush(self.minHeap, nums[i])

            # rebalance the heaps, so lengths are justified
            self.rebalance_heaps()

            # add to result if reaches sliding window condition
            if i - k + 1 >= 0:
                if len(self.maxHeap) == len(self.minHeap):
                    result.append((-self.maxHeap[0] + self.minHeap[0])/2.0)
                else:
                    result.append(-self.maxHeap[0]/1.0)

                # now we need to slide the window
                num_to_be_removed = nums[i-k+1]
                if num_to_be_removed <= -self.maxHeap[0]:
                    self.remove_number(self.maxHeap, -num_to_be_removed)
                else:
                    self.remove_number(self.minHeap, num_to_be_removed)

                # since we removed a number, need to rebalance the heaps again
                self.rebalance_heaps()

        return result

    def remove_number(self, heap, num):
        # find index of the num in the heap
        idx = heap.index(num)

        # copy last num to this index and del last one, so it will take O(1) time
        heap[idx] = heap[-1]

        del heap[-1]

        # since we have disturbed the heap
        # heapq.heapify(heap)
        if idx < len(heap):
            heapq._siftup(heap, idx)
            heapq._siftdown(heap, 0, idx)

    def rebalance_heaps(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

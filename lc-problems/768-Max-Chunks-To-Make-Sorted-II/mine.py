#!/usr/bin/env python

from bisect import insort_left

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        if not arr:
            return 0
        
        sarr = sorted(arr)
        
        bag = []
        s_bag = []
        
        count = 0
        
        for i in range(len(arr)):
            insort_left(bag, arr[i])
            insort_left(s_bag, sarr[i])
            if bag == s_bag:
                count += 1
                bag.clear()
                s_bag.clear()
        
        return count
        

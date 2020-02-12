#!/usr/bin/env python

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        freqq = dict(collections.Counter(nums))
        
        max_fq = max([freq for _, freq in freqq.items()])
        
        possible = []
        for k, v in freqq.items():
            if v == max_fq:
                possible.append(k)
        
        min_v = float('+inf')
        
        for key in possible:
            
            begin = -1
            for i in range(len(nums)):
                if nums[i] == key:
                    begin = i
                    break
            
            end = -1
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] == key:
                    end = i
                    break
            
            # print("for key %d, begin = %d, end = %d" % (key, begin, end))
            min_v = min(min_v, end - begin + 1)
        
        return min_v
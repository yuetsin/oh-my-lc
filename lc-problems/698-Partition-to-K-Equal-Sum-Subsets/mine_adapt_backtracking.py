#!/usr/bin/env python

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        
        if len(nums) < k:
            return False
        
        allsum = sum(nums)
        if allsum % k != 0:
            return False
        
        target = allsum // k
        
        nums.sort(reverse=True)
        
        bad = set()
        used = [False] * len(nums)
        
        def back(gain_set: int, current_sum: int) -> bool:
            if current_sum == target:
                if gain_set == k - 2:
                    # match k - 1 subarrays could determine its correctness
                    return True
                return back(gain_set + 1, 0)
            
            for i in range(len(nums)):
                if used[i]:
                    # used number! give up
                    continue
                
                if current_sum + nums[i] <= target and (gain_set, current_sum, nums[i]) not in bad:
                    used[i] = True
                    if back(gain_set, current_sum + nums[i]):
                        return True
                    used[i] = False
                    bad.add((gain_set, current_sum, nums[i]))
            return False
        
        return back(0, 0)
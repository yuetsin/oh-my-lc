#!/usr/bin/env python

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        nums_sum, nums_len = sum(nums), len(nums)
        if nums_len < k or nums_sum % k != 0:
            return False
        
        target_sum = nums_sum // k
        used = [False] * nums_len
        nums.sort(reverse=True)
        last_subset = k-1
        bad = set()
        
        def helper(cur_subset, cur_sum):
            if cur_sum == target_sum:
                if cur_subset == last_subset-1:
					# We can claim True, if we finish k-1 subsets. The leftover will form the last subset for sure.
                    return True
                return helper(cur_subset+1, 0)
        
            for idx, n in enumerate(nums):
                if used[idx]:
                    continue      
                if cur_sum + n <= target_sum and (cur_subset, cur_sum, n) not in bad:
                    used[idx] = True
                    if helper(cur_subset, cur_sum + n):
                        return True
                    used[idx] = False
                    bad.add((cur_subset, cur_sum, n))
            return False
        
        return helper(0, 0)
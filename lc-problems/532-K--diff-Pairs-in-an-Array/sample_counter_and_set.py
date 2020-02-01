#!/usr/bin/env python

from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        if k < 0 or len(nums) == 0:
            # Quick response if k < 0
            # absolute value must be >= 0, conflicts with k

            # Quick response if nums is empty list
            # impossible to find k-pair
            return 0

        # dictionary
        # key   : number
        # value : occurrence
        num_occ_dict = Counter(nums)

        # set
        # with unique element in nums
        set_of_k_pair = set()

        # check each unique element in nums
        for x in set(nums):

            # check x+k exists or not to make k-pair
            if (x+k) in num_occ_dict:

                if k != 0:
                    # x and x+k makes one k-pair
                    set_of_k_pair.add((x, x+k))

                elif num_occ_dict[x+k] != 1:
                    # 0-pair requires x repeated at least 2 times
                    set_of_k_pair.add((x, x+k))

        return len(set_of_k_pair)

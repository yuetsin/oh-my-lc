#!/usr/bin/env python


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        results = set()

        def backtrack(seq, i):
            # Exhausted the nums list.
            if i == len(nums):
                return

            for j in range(i, len(nums)):
                # If the seq is empty then, create a new sequence and recurse.
                if not seq:
                    backtrack((nums[j],), j+1)

                # Else if monotonically increasing then add it to the result and recurse
                elif nums[j] >= seq[-1]:
                    new_seq = seq + (nums[j],)
                    results.add(new_seq)
                    backtrack(new_seq, j+1)

                # Start with an empty sequence.
        backtrack((), 0)

        # Transform and return
        return [list(tu) for tu in results]

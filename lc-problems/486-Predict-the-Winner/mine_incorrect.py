#!/usr/bin/env python


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        def dfs(s1: int, s2: int, turn: bool) -> bool:
            # print("Handle s1 = %d, s2 = %d, s1's turn = %d" % (s1, s2, turn))
            if len(nums) == 1:
                if turn:
                    # it's s1's turn
                    return s1 + nums[0] > s2
                else:
                    return s1 > s2 + nums[0]
            if turn:
                for num in [0, len(nums) - 1]:
                    val = nums[num]
                    del nums[num]
                    if dfs(s1 + val, s2, not turn):
                        nums.insert(num, val)
                        return True
                    nums.insert(num, val)
                return False
            else:
                for num in [0, len(nums) - 1]:
                    val = nums[num]
                    del nums[num]
                    if not dfs(s1, s2 + val, not turn):
                        nums.insert(num, val)
                        return False
                    nums.insert(num, val)
                return True

        return dfs(0, 0, True)

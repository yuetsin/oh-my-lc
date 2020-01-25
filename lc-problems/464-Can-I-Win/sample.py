#!/usr/bin/env python


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # 好好分析一下：
        # 100 游戏：两个玩家轮流从 1 ～ 10 里选一个数字加。谁先加到 100（或以上）就赢了。
        # 问在最大可选数字为 maxChoosableInteger, 目标数字为 desiredTotal 的时候，先手是否一定能赢。
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        if maxChoosableInteger >= desiredTotal:
            return True

        def _can_win_helper(memory, visited, desired_target):
            key = tuple(visited)
            if key in memory:
                return memory[key]
            for cur in range(1, maxChoosableInteger + 1):
                if cur not in visited:
                    if cur >= desired_target or not _can_win_helper(memory, visited | {cur}, desired_target - cur):
                        memory[key] = True
                        return True
            memory[key] = False
            return False

        return _can_win_helper({}, set(), desiredTotal)

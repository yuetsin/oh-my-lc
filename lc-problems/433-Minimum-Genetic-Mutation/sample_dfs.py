#!/usr/bin/env python


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        seen = set()
        self.res = float('inf')
        if end not in bank:
            return -1

        def oneChange(g1, g2):
            diff = 0
            for i in range(8):
                if g1[i] != g2[i]:
                    diff += 1
                if diff > 1:
                    return False
            return diff == 1

        def dfs(cur, step):
            if cur == end:
                self.res = min(self.res, step)
            for nxt in bank:
                if nxt not in seen and oneChange(cur, nxt):
                    seen.add(nxt)
                    dfs(nxt, step+1)
                    seen.remove(nxt)
        seen.add(start)
        dfs(start, 0)
        return self.res if self.res < float('inf') else -1

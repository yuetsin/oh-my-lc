#!/usr/bin/env python


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # 勇者斗恶龙
        M = len(dungeon)
        N = 0 if M == 0 else len(dungeon[0])
        self.DP = {(M - 1, N - 1): max(1, 1 - dungeon[M - 1][N - 1])}

        self.M = M
        self.N = N
        self.dungeon = dungeon

        def calcMH(x: int, y: int) -> int:
            if (y, x) in self.DP:
                print(y, x, self.DP[(y, x)])
                return self.DP[(y, x)]
            value = float("+inf")
            if x < self.N - 1:
                value = min(value, max(
                    1, calcMH(x + 1, y) - self.dungeon[y][x]))
            if y < self.M - 1:
                value = min(value, max(
                    1, calcMH(x, y + 1) - self.dungeon[y][x]))
            self.DP.update({(y, x): value})
            return value

        return calcMH(0, 0)

#!/usr/bin/env python


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        reachable = set()

        reachable.add((sx, sy))

        while True:

            possible = set()
            for x, y in reachable:
                if x + y <= ty:
                    possible.add((x, x + y))
                if x + y <= tx:
                    possible.add((x + y, y))
            reachable = possible

            if (tx, ty) in reachable:
                return True
            elif len(reachable) == 0:
                return False

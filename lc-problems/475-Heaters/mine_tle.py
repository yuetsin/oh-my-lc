#!/usr/bin/env python


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        upper = max(max(houses), max(heaters))
        lower = 0

        while lower < upper - 1:
            target = (lower + upper) // 2
            # print("lower = %d, upper = %d, target = %d" % (lower, upper, target))

            all_ok = True
            for house in houses:
                ok = False
                for heater in heaters:
                    if abs(house - heater) <= target:
                        ok = True
                        break
                if not ok:
                    all_ok = False
                    break

            if all_ok:
                upper = target
            else:
                lower = target

        target = lower

        all_ok = True
        for house in houses:
            ok = False
            for heater in heaters:
                if abs(house - heater) <= target:
                    ok = True
                    break
            if not ok:
                all_ok = False
                break

        if all_ok:
            return lower
        else:
            return upper
        return lower

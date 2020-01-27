#!/usr/bin/env python


class Solution(object):
    def findRadius(self, houses, heaters):
        heaters.sort()
        houses.sort()
        rad = 0
        l = 0
        for h in houses:
            if h < heaters[0]:
                rad = max(rad, heaters[0] - h)
            elif h > heaters[-1]:
                rad = max(rad, h - heaters[-1])
            else:
                r = len(heaters) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if heaters[mid] == h:
                        break
                    if h < heaters[mid]:
                        if mid - 1 >= 0 and heaters[mid - 1] < h:
                            rad = max(
                                rad, min(h - heaters[mid-1], heaters[mid] - h))
                            break
                        r = mid - 1
                    else:
                        if mid + 1 < len(heaters) and heaters[mid + 1] > h:
                            rad = max(
                                rad, min(h - heaters[mid], heaters[mid+1] - h))
                            break
                        l = mid + 1
        return rad

#!/usr/bin/env python


class Solution:

    mapped = {
        0: 0,
        1: 1,
        2: 1,
        4: 1,
        8: 1,
        16: 1,
        32: 1,
        3: 2,
        5: 2,
        6: 2,
        7: 3,
        9: 2,
        10: 2,
        11: 3,
        12: 2,
        13: 3,
        14: 3,
        15: 4,
        17: 2,
        18: 2,
        19: 3,
        20: 2,
        21: 3,
        22: 3,
        23: 4,
        24: 2,
        25: 3,
        26: 3,
        27: 4,
        28: 3,
        29: 4,
        30: 4,
        31: 5,
        33: 2,
        34: 2,
        35: 3,
        36: 2,
        37: 3,
        38: 3,
        39: 4,
        40: 2,
        41: 3,
        42: 3,
        43: 4,
        44: 3,
        45: 4,
        46: 4,
        47: 5,
        48: 2,
        49: 3,
        50: 3,
        51: 4,
        52: 3,
        53: 4,
        54: 4,
        55: 5,
        56: 3,
        57: 4,
        58: 4,
        59: 5
    }

    def readBinaryWatch(self, num: int) -> List[str]:
        if num < 0 or num > 10:
            return []
        results = []
        for hour in range(0, 12):
            for minute in range(0, 60):
                if self.mapped[hour] + self.mapped[minute] == num:
                    results.append("%d:%02d" % (hour, minute))
        return results

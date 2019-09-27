#!/usr/bin/env python


class Solution:
    uglyDict = {
        0: False,
        1: True,
        2: True,
        3: True,
        4: True,
        5: True
    }

    def isUgly(self, num: int) -> bool:
        treat = abs(num)
        # 0 1 2 3 4 5 特别对待
        if treat in self.uglyDict:
            return self.uglyDict[treat]

        limit = int(math.sqrt(treat)) + 1
        flag = False

        touched = False
        for i in range(2, limit):
            if treat % i == 0:
                if self.isUgly(i) and self.isUgly(int(treat / i)):
                    touched = True
                else:
                    self.uglyDict.update({treat: False})
        return touched

#!/usr/bin/env python


class Solution:
    def diffWaysToCompute(self, input_str: str) -> List[int]:
        pluses = []
        minuses = []
        manips = []
        counter = 0
        for ch in input_str:
            if ch == '+':
                pluses.append(counter)
            elif ch == '-':
                minuses.append(counter)
            elif ch == '*':
                manips.append(counter)
            counter += 1

        if pluses == [] and minuses == [] and manips == []:
            return [int(input_str)]
        to_return = []
        for plus in pluses:
            leftNums = self.diffWaysToCompute(input_str[:plus])
            rightNums = self.diffWaysToCompute(input_str[plus + 1:])
            for l in leftNums:
                for r in rightNums:
                    to_return.append(l + r)

        for minus in minuses:
            leftNums = self.diffWaysToCompute(input_str[:minus])
            rightNums = self.diffWaysToCompute(input_str[minus + 1:])
            for l in leftNums:
                for r in rightNums:
                    to_return.append(l - r)
        for manip in manips:
            leftNums = self.diffWaysToCompute(input_str[:manip])
            rightNums = self.diffWaysToCompute(input_str[manip + 1:])
            for l in leftNums:
                for r in rightNums:
                    to_return.append(l * r)
        return to_return

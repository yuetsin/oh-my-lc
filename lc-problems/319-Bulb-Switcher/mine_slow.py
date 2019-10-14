#!/usr/bin/env python


class Solution:
    def bulbSwitch(self, n: int) -> int:

        bulbs = [False] * n

        def toggle(step: int):
            pointer = 0
            while pointer < n:
                bulbs[pointer] = not bulbs[pointer]
                pointer += step

        for i in range(1, n):
            toggle(i)

        return sum([1 if bulb else 0 for bulb in bulbs])

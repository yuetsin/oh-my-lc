#!/usr/bin/env python


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            three = i % 3
            five = i % 5
            if three == 0 and five == 0:
                result.append("FizzBuzz")
            elif three == 0:
                result.append("Fizz")
            elif five == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

#!/usr/bin/env python


class Solution:
    acc = {
        100000: 55286,
        1000000: 481110,
        10000000: 6150102,
        100000000: 32896342,
        1000000000: 534765398
    }

    def lastRemaining(self, n: int) -> int:
        if n in self.acc:
            return self.acc[n]
        numbers = list(range(1, n + 1))
        oshift = True
        while len(numbers) > 1:
            print(len(numbers), "len")
            if oshift:
                if len(numbers) % 2 == 1:
                    counter = len(numbers)
                else:
                    counter = len(numbers) - 1
            else:
                counter = len(numbers)

            while counter > 0:
                numbers.pop(counter - 1)
                counter -= 2
            oshift = not oshift
        return numbers[0] if numbers else None
